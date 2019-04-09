# Copyright 2019 Tecnativa - Cristina Martin R.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Welcome mail to new subscribers",
    "summary": "Send an automated welcome mail to new newsletter subscribers",
    'license': 'AGPL-3',
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'category': 'Social',
    'version': '11.0.1.0.0',
    'website': 'https://github.com/OCA/social',
    'depends': [
        'mass_mailing',
        'base_automation',
    ],
    'data': [
        "data/base_automation_data.xml",
    ],
    'application': False,
    'installable': True,
}
