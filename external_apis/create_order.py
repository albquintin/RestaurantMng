url = 'http://localhost:8069'
db = 'odoo'
username = 'admin'
password = 'admin'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()

uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

new_order = models.execute_kw(db, uid, password,
    'restaurantmng.order', 'create',
    [{'order_number': '1234', 'client_id':'1','delivery_id':'1'}])
