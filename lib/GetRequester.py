import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        content_list = []
        json_content = json.loads(self.get_response_body())
        for content in json_content:
            content_list.append(content)
        return content_list
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()

print(get_requester.get_response_body())