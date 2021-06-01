url = 'http://localhost:8069'
db = 'odoo'
username = 'admin'
password = 'admin'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
vegan_numbers = models.execute_kw(db, uid, password,
    'restaurantmng.dish', 'search',
    [[['is_vegan', '=', True]]])
print(vegan_numbers)

vegan_count = models.execute_kw(db, uid, password,
    'restaurantmng.dish', 'search_count',
    [[['is_vegan', '=', True]]])
print(vegan_count)

vegan_details = models.execute_kw(db, uid, password,
    'restaurantmng.dish', 'search_read',
    [[['is_vegan', '=', True]]],
    {'fields': ['name', 'ingredient_ids', 'price'], 'limit': 5})
print(vegan_details)