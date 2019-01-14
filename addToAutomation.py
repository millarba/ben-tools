import requests
import json

print('Hello world!')

#add contact list here
contacts = ["ben", "kelsey"]
#add seriesid
seriesid = "2"

for contact in contacts:
	payload = {
				'contactAutomation' :{
						'contact': contact,
						'automation': seriesid
					}
				}
	#api key here
	params = {'api_key' : <API_KEY>, 'Content-Type' : 'application/x-www-form-urlencoded'}
	#account url here
	r = requests.post('https://<API_URL>.api-us1.com/api/3/contactAutomations', params=params, data=json.dumps(payload))

	print(payload['contactAutomation']['contact'])
	print(r.status_code)
	print(r.text)