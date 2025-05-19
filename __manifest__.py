{
    'name': 'library books',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Simple module pour livre',
    'author': 'Thomas Leconte',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}