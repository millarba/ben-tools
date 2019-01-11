import requests

print("Hello world!")

r = requests.get('https://api.github.com/events')

print(r.text)