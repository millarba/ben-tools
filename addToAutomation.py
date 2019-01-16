import requests
import json

print('Hello world!')

#add contact list here
contacts = []
#add seriesid
seriesid = ""

total_attempted = len(contacts)
total_successful = 0

for contact in contacts:
	payload = {
				'contactAutomation' :{
						'contact': str(contact),
						'automation': seriesid
					}
				}
	#api key here
	params = {'api_key' : <API-KEY>, 'Content-Type' : 'application/x-www-form-urlencoded'}
	#account url here
	r = requests.post('https://<API-URL>.api-us1.com/api/3/contactAutomations', params=params, data=json.dumps(payload))

	print('Contact ID: ' + payload['contactAutomation']['contact'])
	print(r.status_code)
	# print(r.json())

	if int(r.status_code) == 201:
		total_successful += 1

print(str(total_successful) + ' out of ' + str(total_attempted) + ' were successful')