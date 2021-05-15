from odoo import models, fields

class Staff(models.Model):
    _name = 'restaurantmng.staff'

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    address = fields.Char()
    mobile_phone = fields.Char()
    salary = fields.Integer(string="Salary (in €, annual)")
    starting_date = fields.Date()

class Manager(models.Model):
    _name = 'restaurantmng.manager'
    _order = 'name'
    _inherit = 'restaurantmng.staff'

    years_experience = fields.Integer()
    working_area = fields.Char()

class Chef(models.Model):
    _name = 'restaurantmng.chef'
    _order = 'name'
    _inherit = 'restaurantmng.staff'

    specialty = fields.Char()
