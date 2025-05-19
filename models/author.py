from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string="Nom Auteur", required=True)
    birth_date = fields.Date(string="Date de Naissance")
    nationality = fields.Char(string="Nationnalité")
