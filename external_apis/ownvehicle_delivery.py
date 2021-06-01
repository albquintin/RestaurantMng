url = 'http://localhost:8069'
db = 'odoo'
username = 'admin'
password = 'admin'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("details...", version)

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

delivery_count = models.execute_kw(db, uid, password,
    'restaurantmng.delivery', 'search_count',
    [[['own_vehicle', '=', True]]])
print(delivery_count)

delivery_details = models.execute_kw(db, uid, password,
    'restaurantmng.delivery', 'search_read',
    [[['non_gluten', '=', True]]],
    {'fields': ['name', 'dni', 'mobile_phone'], 'limit': 5})
print(delivery_details)