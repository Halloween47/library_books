from odoo import models, fields

class LibraryBook(models.Model):
        _name = 'library.book'
        _description = 'Book'

        title = fields.Char(string="Titre", required=True)
        author = fields.Char(string="Author")
        page_count = fields.Integer(string="Nombre de pages")
        available = fields.Boolean(string="Disponible", default=True)