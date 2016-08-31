
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/users/test_page'] = 'Users#test_page'
routes['GET']['/users/get_data'] = 'Users#get_data'
# routes['POST']['/users/get_data'] = 'Users#get_movie'
