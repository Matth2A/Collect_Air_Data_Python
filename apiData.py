import requests

class apiData:

    # Constructors
    def __init__(self, apiUrl, endpoint, request_body):
        self.apiUrl = apiUrl
        self.endpoint = endpoint
        self.request_body = request_body


    # Setters
    # Set the API URL
    def setApiUrl(self, apiUrl):
        self.apiUrl = apiUrl


    # Set the endpoint
    def setEndpoint(self, endpoint):
        self.endpoint = endpoint


    # Set the request body
    def setRequestBody(self, request_body):
        self.request_body = request_body


    # Fetch the API data using a POST request
    def getApiDataPost(self):
        return requests.post(self.apiUrl+self.endpoint, json=self.request_body)


    # Fetch the API data using a GET request
    def getApiDataGet(self):
        return requests.get(self.apiUrl+self.endpoint, json=self.request_body)