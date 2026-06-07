from odoo import models, fields

class Student(models.Model):
    _name = "student"
    _description = "Student"
    _order = "age desc"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    