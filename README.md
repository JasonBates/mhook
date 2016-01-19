## Mondo Foursquare Webhook 1.0

Basic foursquare checkin python script

powered by flask it provides a web hook end point

1. Receive a notification of a transaction
2. Do a foursquare lookup based on the merchant name and latitude / longitude
3. Use fuzzy matching to compare the most likely venue with the merchant name
4. If it's a reasonably good match do a checkin

This script needs a Mondo ClientID / Secret and a Foursquare Oauth key
saved in the config file : 4sq.json-template which should be renamed to 4sq.json
