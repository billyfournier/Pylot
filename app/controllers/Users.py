from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('UserModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')
    def test_page(self):
        return self.load_view('test.html')

    def get_data(self):
        data = self.models['UserModel'].get_data()
        print data
        return data
