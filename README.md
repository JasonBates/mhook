## Mondo Foursquare Webhook 1.0

Basic foursquare checkin python script

powered by flask it provides a web hook end point
for receiving a transaction webhook, checking for a foursquare location
and checking in through the foursquare API.

The code is self explanatory, but basically the steps are:

1. Receive a notification of a transaction
2. Do a foursquare lookup based on the merchant name and latitude / longitude
3. Use fuzzy matching (fuzzywuzzy) to compare the response with the merchant name
4. If it's a reasonably good match do a checkin through the foursqaure API.

This script needs a Mondo ClientID / Secret and a Foursquare Oauth key
saved in the config file : 4sq.json-template which should be renamed to 4sq.json

You can generate the Oauth key with Postman once you've set up a Foursquare app / developer account.

Python libraries required : requests, flask, fuzzywuzzy.

(I use nginx / Gunicorn to run it through WSGI in the wild)
