from flask import Flask, request, json
import requests
from fuzzywuzzy import fuzz

application = Flask(__name__)

foursquare_checkinURL = "https://api.foursquare.com/v2/checkins/add"
foursquare_lookupURL = "https://api.foursquare.com/v2/venues/search"

try:
    with open('./4sq.json') as data_file:
        config = json.load(data_file)
except IOError:
    raise Exception('No config.json file found')

def foursquare_lookup(merchant_name, merchant_lat, merchant_lon):
    params = {
                "query": merchant_name,
                "ll": str(merchant_lat)+","+str(merchant_lon),
                "client_id": config['client_id'],
                "client_secret": config['client_secret'],
                "limit": "2",
                "intent": "checkin",
                "radius": "1000",
                "v": "20151212"
            }
    # print json.dumps(params)
    return requests.get(foursquare_lookupURL, params=params, verify=False).json()


def foursquare_checkin(venue_id):
    params = {
              "shout": "Mondo checkin!",
              "broadcast": "public",
              "oauth_token": config['oauth_token'],
              "venueId": venue_id,
              "v": "20151212"
             }
    checkin_response = requests.post(foursquare_checkinURL, params=params)
    return str(checkin_response.ok)

@application.route('/')
def route_test():
    return "This works then"

@application.route('/hook', methods=['POST'])
def print_post():
    print("post received")
    trx = request.get_json()

    merchant_name = trx['data']['merchant']['name']
    merchant_lat = trx['data']['merchant']['address']['latitude']
    merchant_lon = trx['data']['merchant']['address']['longitude']

    fsq_response = foursquare_lookup(merchant_name, merchant_lat, merchant_lon)
    print("foursquare request made")
    # check there is a venue returned
    try:
        foursq_name = fsq_response['response']['venues'][0]['name']
        foursq_venue = fsq_response['response']['venues'][0]['id']
    except IndexError:
        print('no match')
        return 'no match from 4Sq lookup'

    # Check if the first returned venue is a fuzzy match with merchant name
    match = fuzz.partial_ratio(merchant_name, foursq_name)
    if match >= 80:
        print('Checkin at ' + foursq_name + " " + str(match))
        checkin_action = foursquare_checkin(foursq_venue)
        return "checked in :" + checkin_action
    else:
        print("no match: " + foursq_name + " + " + merchant_name + " " + str(match))
        return "no fuzzy match on :" + foursq_name + " + "+ merchant_name


if __name__ == "__main__":

    application.run(host='0.0.0.0')
