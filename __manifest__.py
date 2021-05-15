{
    'name': "Restaurantmng",

    'summary': """Manage Restaurants""",

    'description': """
        Module for CA to manage a restaurant:
            - employees
            - deliveries
            - events
    """,

    'author': "Alberto Quintin",
    'website': "http://www.restaurantmng.com",

    'category': 'Test',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/restaurant.xml',
        'views/staff.xml',
    ],
}