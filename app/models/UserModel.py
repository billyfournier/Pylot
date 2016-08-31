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
        api_response = requests.get('http://api.nal.usda.gov/ndb/reports/?ndbno=01009&type=b&format=json&api_key='+api_key).content
        return api_response
