from odoo import models, fields

class IssueCategory(models.Model):
    _name = 'issue.tags'
    _description = 'Issue Tags'

    name = fields.Char('Tag Name', required=True)
    description = fields.Html('Description')
    active = fields.Boolean('Active', default=True)
    plm_created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    plm_created_date = fields.Datetime('Creation Date', default=fields.Datetime.now)
