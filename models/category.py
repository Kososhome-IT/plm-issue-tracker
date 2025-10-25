from odoo import models, fields

class IssueCategory(models.Model):
    _name = 'issue.category'
    _description = 'Issue Category'

    name = fields.Char('Category Name', required=True)
    description = fields.Html('Description')
    active = fields.Boolean('Active', default=True)
    plm_created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    plm_created_date = fields.Datetime('Creation Date', default=fields.Datetime.now)
