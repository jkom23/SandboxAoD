# Intro to APIs
## Background
![Several clients connect to a server via HTTP](img/server_clients.png)
1. What does **HTTP** stand for, and what does it mean in the context of the _internet_?
   Hyper Text Transfer Protocols (like a program/algorithm, related to data stream), it allows different systems to communicate and transfer information
2. What is the relationship between a **server** and **clients**?
   The server holds data and the client accesses the server to request data with an HTTP data request
3. In the context of this diagram and APIs (application programing interface, how you can access the server), what is a **URL**?
   Uniform resource locater, it tells the server (via the API) to take the user to a certain web page (place on the server), takes you to a certain endpoint (certain port)
4. In the context of this diagram and APIs, what is an **endpoint**?
 Endpoints are the ports where the clients can access data on the server

## Server-Client Communication
Let's examine an interaction between a server and a client.
![A client sends a GET request to a server, who provides the item after authenticating the client](img/server_client.png)
1. How does the server know who the client is?
   It provides a key that lets the server know the clients identity
2. Why does the server need a `KEY` before sending `X`?
   Otherwise it could send private data to the wrong person; paywall; spamming server requests
3. The server and client are communicating via HTTP (Hyper _Text_ Transfer Protocol). What format will the requested `X` be sent as?
    We will get X as a .json object
## Data Transfer
### Review
Examine the following Python dictionary.
```py
pokemon = {
    'name': "Scolipede",
    'height': 25,
    'types': [
        {
            'slot': 1,
            'type': "bug"
        },
        {
            'slot': 2,
            'type': "poison
        }
    ]
}
```
1. What does `pokemon['name']` evaluate to?
   Scolipede
2. What does `pokemon['types']['0']` evaluate to?
   Dictionary of the first item in types dictionary, with key value pairs of slot:1 and type:bug
3. Write Python code that accesses the `height`.
   pokemon['height']
4. Write Python code that accesses the `type` in slot 2.
   pokemon['types'][1]['type']

### JSON
1. What does **JSON** stand for? Why is it useful for **REST** APIs?
Java Script Object Notation. it is useful for Representational state transfer because it can easily deliver data and is readable by any language; easy to parse
Also SOAP APIs exist 
Examine the following **Javascript object**.
```js
pokemon = {
    'name': "Scolipede",
    'height': 25,
    'types': [
        {
            'slot': 1,
            'type': "bug"
        },
        {
            'slot': 2,
            'type': "poison
        }
    ]
}
```

2. What does `pokemon['name']` evaluate to?
   Scolipede
3. How would you access the `type` in slot 2?
 pokemon['types'][0]['type']
5. How is a Javascript object different than a Python dictionary?
   Very similar

## Consuming APIs With Python
Let's return to this diagram:  
![A client sends a GET request to a server, who provides the item after authenticating the client](img/server_client.png)  
and accompany it with some Python code:
```python
import requests
BASE_URL = "http://www.server.com/"
ENDPOINT = "endpoint"
API_KEY = "abcd1234"

payload = {'key': API_KEY, 'q': "X"}

response = requests.get(BASE_URL+ENDPOINT, params=payload) #params not always needed
if response.ok:
    data = response.json()
else:
    print(reponse.status_code, response.text)
```

1. What is the **requests** module used for?
   making an API data request
2. What parameters does the `get` method take?
   URL with an endpoint and parameters (key, payload, query)
3. What is a **payload** in the context of APIs?
   All of the information, sent as dictionary string, that you will send to the API in order to get your request
4. We can now treat `data` as a Python dictionary. Why is that allowed?
   Because .json can be converted to a pyhton dictionary so we can read it easily
5. How do we check if the response is OK?
   check the response.status_code
6. What do we do if the response is not OK?
    we read the response.text
7. What is an HTTP **status code**?
   an error code (ex. 404 not found)