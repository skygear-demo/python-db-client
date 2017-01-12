import os
import json
import requests
import uuid

class SkyHandler(object):
    retry_login = 0

    def __init__(self):
        if os.getenv('ENDPOINT') is None:
            print("Please make sure endpoint is given in environment variables.")
            quit()
        self.url = os.getenv('ENDPOINT')
        self.headers = {'Content-Type': 'application/json'}
        self.access_token = None
        self.get_access_token('login')

    def get_access_token(self, action):
        api_key = os.getenv('API_KEY')
        username = os.getenv('USER_NAME')
        email = os.getenv('USER_EMAIL')
        password = os.getenv('USER_PASSWORD')
        action = "auth:" + action
        if api_key and username and email and password:
            datajson = {
                "api_key": api_key,
                "action": action,
                "username": username,
                "email": email,
                "password": password
            }
            response = self.post_request(datajson)
            if (self.retry_login == 0 and 'error' in response
                and response['error']['code'] == 110):
                self.get_access_token('signup')
                self.retry_login = 1
            elif 'result' in response and 'access_token' in response['result']:
                self.access_token = response['result']['access_token']
        else:
            print("Fail to get access token. Please make sure environment variables are given correctly.")
            quit()

    def update_record(self, record_type, record_id, key, value):
        if self.access_token is None:
            self.get_access_token('login')
        if self.access_token is not None:
            record_id = record_type + "/" + record_id
            datajson = {
                "action": "record:save",
                "database_id": "_private",
                "access_token": self.access_token,
                "records": [{
                    "_id": record_id,
                    key: value
                }]
            }
            response = self.post_request(datajson)
            if 'result' in response:
                return response['result']

    def search_record(self, record_type, key, value, col):
        if self.access_token is None:
            self.get_access_token('login')
        if self.access_token is not None:
            datajson = {
                "action": "record:query",
                "access_token": self.access_token,
                "database_id": "_private",
                "record_type": record_type,
                "predicate": [
                    "eq", {"$type": "keypath", "$val": key}, value
                ]
            }
            response = self.post_request(datajson)
            if ('result' in response and len(response['result'])
                and col in response['result'][0]):
                result = response['result'][0][col]
                if col == '_id':
                    return result.split('/')[1]
                return result

    def post_request(self, datajson):
        filename = str(uuid.uuid4()).replace('-', '')
        with open(filename, 'w') as datafile:
            json.dump(datajson, datafile)
        with open(filename) as data:
            r = requests.post(self.url, headers=self.headers, data=data)
            response = r.json()
        os.remove(filename)
        print(response)
        return response
