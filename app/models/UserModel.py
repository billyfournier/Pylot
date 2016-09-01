from system.core.model import Model
import requests

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()

    def get_data(self):
        with open('.api_key') as infile:
            api_key = infile.readline().rstrip()
        # this comes from 'import requests'
        # can access the json data of this request through the 'text' attribute
        api_response = requests.get('http://api.nal.usda.gov/ndb/reports/?format=json&ndbno=01009&type=b&api_key='+api_key).content
        return api_response

    def get_food_data(self):
        with open('.api_key') as infile:
            api_key = infile.readline().rstrip()
        api_query =  'http://api.nal.usda.gov/ndb/reports/'
        api_query += '?type=b&format=json'
        api_query += '&ndbno='    + '01009'
        api_query += '&api_key='  + api_key
        api_response = requests.get(api_query).content
        return api_response

    def get_food_list(self):
        with open('.api_key') as infile:
            api_key = infile.readline().rstrip()
        api_query =  'http://api.nal.usda.gov/ndb/list?'
        api_query += 'format=json&lt=f&max=1000'+api_key
        api_response = requests.get(query)
        return api_response
