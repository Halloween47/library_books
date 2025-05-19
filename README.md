# 📚 Odoo Module - Library Books

Ce module simple permet de gérer une liste de livres dans Odoo.

## 🔧 Fonctionnalités

- Création de livres avec :
  - Titre
  - Auteur (relation Many2one)
  - Nombre de pages
  - Disponibilité (boolean)
- Vue kanban personnalisée avec mise en valeur des livres non disponibles
- Déploiement prêt pour Docker
- Code structuré et documenté

## 🧪 Installation

1. Cloner ce dépôt dans le dossier `addons` de votre instance Odoo.
2. Mettre à jour la liste des modules depuis l'interface Odoo.
3. Installer le module `Library Books`.

## 🐳 Environnement recommandé

Utiliser Docker avec le fichier `docker-compose.yml` suivant :

```yaml
version: '3.1'

services:
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

  odoo:
    image: odoo:16
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - ./addons:/mnt/extra-addons
      - odoo-web-data:/var/lib/odoo
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo

volumes:
  odoo-db-data:
  odoo-web-data:
```

## ✍️ Auteur

Jean-Louis — Développeur freelance front-end / intégrateur Odoo débutant