import requests
from requests.exceptions import HTTPError
from getpass import getpass

requests.get('https://api.github.com')
# Here we are calling the GET request method that retrieves data from a URL.
# We are requesting data from GitHub's root REST API.

# We can store the data recieved by GET in a 'response' object:
response = requests.get('https://api.github.com')

# and this response object has various fields we can access:
response.status_code
# 'status_code' holds a number code that tells us the status of a request
# 200 is 'ok' and 404 means 'not found'

# We can also import HTTPError to raise an error for certain status_code values with the following:
# 'from requests.exceptions import HTTPError'

# This for block attempts to get a response from a valid, an invalid url
# If an http error is found from the status code, it will print that http error
for address in ['https://api.github.com', 'https://api.github.com/blahblahblah']:
    try:
        response = requests.get(address)
        response.raise_for_status()
    except HTTPError as error:
        print(f'HTTP Error: {error}')
    except Exception as other_error:
        print(f'Other error: {other_error}')
    else:
        print('Request and response successful')
# Running this should result in one successful response and one HTTP error (404)

# To access the 'payload'(message body) of a response, you can call 'content' or 'text'
# 'content' will return the content in raw bytes, while 'text' will reutrn a str
response = requests.get('https://api.github.com')
print('\nPayload of response in bytes:\n')
print(response.content)
print('\nPayload of response in string:\n')
print(response.text)

# However, the most convienient way to access data in a response is to make a dictionary out of the
# the data using JSON
payload = response.json()
print(f'\nCurrent_user_url value of dictionary created from response payload: {payload["current_user_url"]}')

# The 'header' of the response also contains important information such as server name, date,
# and content type. This can be accessed by calling 'headers' on response which returns a dictionary-like output:
headers = response.headers
print(f'\nServer name from header: {headers["Server"]}\n')

# The POST function allows you to send data to a specific url
# The payload of the POST message is passed as a parameter of a dictionary, list of tuples, bytes or file type object
response = requests.post('https://httpbin.org/post', data={'key': 'value'})

# You can verify fields of your request by calling 'request' on your response
print(response.request.url)
print(response.request.body)

# If you want to maintain a persistent connection with a server, you can call 'Session'
# Your app keeps your session connection saved so you can access the session again and the app will reuse the connection
with requests.Session() as session:
    # authorization function to login (insert your username):
    session.auth = ('<your github username here>', getpass())
    response = session.get('https://api.github.com/user')

# With session, you can access data in your response the same as before:
print(response.headers)
print(response.json())
# You can see that the response contains information on your github account which you can access just like before

# Thank you for reading!