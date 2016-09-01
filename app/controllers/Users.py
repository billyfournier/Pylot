from system.core.controller import *
import json
from pprint import pprint

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('UserModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')
    def test_page(self):
        return self.load_view('test.html')
    def main(self):
        items = self.models['UserModel'].get_list()
        items = json.loads(items)
        return self.load_view('main.html', foods=items['list']['item'])

    def get_data(self):
        data = self.models['UserModel'].get_data()
        return data
    def get_list(self):
        data = self.models['UserModel'].get_list()
        return self.load_view('main.html')
    def get_group(self):
        data = self.models['UserModel'].get_group(request.form)
        return '1'
