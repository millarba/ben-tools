import requests
import json

print('Hello world!')

payload = {
			'contactAutomation' :{
					'contact': <CONTACT_ID>,
					'automation': <SERIES_ID>
				}
			}

params = {'api_key' : <API_KEY>, 'Content-Type' : 'application/x-www-form-urlencoded'}

r = requests.post('https://<API_URL>.api-us1.com/api/3/contactAutomations', params=params, data=json.dumps(payload))

print(payload['contactAutomation']['contact'])
print(r.status_code)
print(r.text)