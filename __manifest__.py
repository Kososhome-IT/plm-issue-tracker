{
    'name': 'PLM Issue Tracker',
    'version': '1.0',
    'summary': 'Module to Raise Request and queries',
    'author': 'Akash Sagar',
    'category': 'Messaging',
    'depends': ['sale_management','product','inspection', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml', 
        'views/category_views.xml',
        'views/tags_view.xml',
        'views/issue_tracker_view.xml',
    ],
    'installable': True,
    'application': True,
}
