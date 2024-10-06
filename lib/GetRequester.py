import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Return raw bytes instead of decoding to match test expectation
        response = requests.get(self.url)
        return response.content  # Return as byte string

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)  # Convert the byte string to a Python dict or list
