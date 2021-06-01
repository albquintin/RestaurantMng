{
    'name': "Restaurantmng",

    'summary': """Manage Restaurants""",

    'description': """
        Module to manage a single restaurant. You will be able to manage your staff, deliveries and clients in the same module
    """,

    'author': "Alberto Quintin",
    'website': "http://www.restaurantmng.com",

    'category': 'Test',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/restaurant.xml',
        'views/staff.xml',
        'views/ingredient.xml',
        'views/dish.xml',
        'views/menu.xml',
        'views/drink.xml',
        'views/equipment.xml',
        'views/supplier.xml',
        'views/supply_order.xml',
        'views/client.xml',
        'views/neighborhood.xml',
        'views/order.xml',
        'views/event.xml',
        'reports/report_event.xml',
        'reports/report_order.xml',
        'reports/report_food_order.xml',
        'reports/report_drink_order.xml',
        'reports/report_equipment_order.xml',
    ],
}