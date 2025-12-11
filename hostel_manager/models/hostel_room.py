from odoo import models, fields

# class BaseArchive(models.AbstractModel):
#     _name = 'base.archive'
#     _description = 'Archive Behavior'
#     es =fields.Char(string='testing')
#     active = fields.Boolean(default=True)
#
#     def do_archive(self):
#         for record in self:
#             record.active = not record.active


class HostelRoom(models.Model):
    _name = 'hostel.room'
    # _inherit = 'base.archive'
    _description = 'Hostel Room'

    name = fields.Char(string='Room Number', required=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')],
        string='Room Type', default='single')
    capacity = fields.Integer(string='Capacity', default=1)
    price_per_day = fields.Float(string='Price per Day')
    is_available = fields.Boolean(string='Available', default=True)
    student_ids = fields.One2many('hostel.allocation', 'room_id', string='Allocated Students')
