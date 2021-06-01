url = 'http://localhost:8069'
db = 'odoo'
username = 'admin'
password = 'admin'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()

uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

vip_count = models.execute_kw(db, uid, password,
    'restaurantmng.client', 'search_count',
    [[['is_vip', '=', True]]])
print(vip_count)

vip_details = models.execute_kw(db, uid, password,
    'restaurantmng.client', 'search_read',
    [[['is_vip', '=', True]]],
    {'fields': ['name', 'neighborhood_id', 'mobile'], 'limit': 5})
print(vip_details)