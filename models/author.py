from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string="Author Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    nationality = fields.Char(string="Nationality")
