import requests

url = 'http://localhost:5000/api'
input_string = 'Peter File'
data = {'input_string': input_string}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('String successfully sent to the server.')
elif response.status_code == 400:
    print('Bad request. Please provide a valid input string.')
else:
    print(f'Error sending the string. Status code: {response.status_code}')