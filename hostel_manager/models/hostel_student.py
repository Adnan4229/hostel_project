from odoo import models, fields

class HostelStudent(models.Model):
    _name = 'hostel.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hostel Student'

    name = fields.Char(string='Student Name', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    course = fields.Char(string='Course')
    contact_no = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    allocation_ids = fields.One2many('hostel.allocation', 'student_id', string='Room Allocations')

