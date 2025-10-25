from odoo import models, fields, api


class IssueTracker(models.Model):
    _name = 'issue.tracker'
    _description = 'Issue Tracker'
    _inherit = ['mail.thread', 'mail.activity.mixin'] 

    # name = fields.Char('Title', required=True)
    name = fields.Char('Title', required=True, readonly=True, copy=False, default='New', tracking=True)
    category_id = fields.Many2one(
        'issue.category', 
        string='Category',
        ondelete='set null'
    )
    product_id = fields.Many2one(
        'product.template', 
        string='Product',
    )
    tags_ids = fields.Many2many(
        'issue.tags',        
        'issue_tracker_tag_rel',
        'issue_id',
        'tag_id',
        string='Tags'
    )
    
    sku = fields.Char('SKU')
    plm_mail_subject = fields.Char('Mail Subject')
    description = fields.Html('Description')
    
    # Fixed: Priority as Selection (for widget="priority" in tree view)
    plm_priority = fields.Selection([
        ('0', 'Not Set'),
        ('1', 'For Information'),
        ('2', 'Low'),
        ('3', 'Medium'),
        ('4', 'High'),
        ('5', 'Critical'),
    ], string='Priority', default='0')
    
    vendor_id = fields.Many2one(
        'res.partner',
        string='Vendor',
        domain=[('is_company', '=', True), ('supplier_rank', '>', 0)]
    )
    
    state = fields.Selection([
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('reject', 'Rejected'),
    ], default='new', string="State", tracking=True)
    
    assigned_user_id = fields.Many2one('res.users', string='Assigned To')
    plm_created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)
    plm_created_date = fields.Datetime('Created On', default=fields.Datetime.now, readonly=True)
    plm_assigned_on = fields.Datetime('Assigned On')
    plm_deadline_date = fields.Datetime('Deadline Date')
    plm_updated_date = fields.Datetime('Last Updated', default=fields.Datetime.now, readonly=True)

    @api.model
    def create(self, vals):
        # Auto-generate sequence number
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('issue.tracker') or 'New'
        
        vals['plm_created_by'] = self.env.uid
        vals['plm_created_date'] = fields.Datetime.now()
        vals['plm_updated_date'] = fields.Datetime.now()
        return super(IssueTracker, self).create(vals)

    def write(self, vals):
        vals['plm_updated_date'] = fields.Datetime.now()
        return super(IssueTracker, self).write(vals)
