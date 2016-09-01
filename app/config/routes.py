
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/users/test_page'] = 'Users#test_page'
routes['GET']['/users/get_data'] = 'Users#get_data'

routes['GET']['/users/get_list'] = 'Users#get_list'
routes['GET']['/users/main'] = 'Users#main'
# routes['POST']['/users/get_data'] = 'Users#get_movie'

# routes['GET']['/users/get_group'] = 'Users#get_group'
routes['POST']['/users/get_group'] = 'Users#get_group'
