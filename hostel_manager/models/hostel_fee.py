from odoo import models, fields

class HostelFee(models.Model):
    _name = 'hostel.fee'
    _description = 'Hostel Fee'

    allocation_id = fields.Many2one('hostel.allocation', string='Allocation', required=True)
    amount = fields.Float(string='Amount', required=True)
    paid = fields.Boolean(string='Paid', default=False)
    payment_date = fields.Date(string='Payment Date')
