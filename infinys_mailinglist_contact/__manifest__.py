# -*- coding: utf-8 -*-
{
    'name': "infinys_mailinglist_contact",

    'summary': """
        Enhance Your Email Marketing with Advanced Mailing contact Features
    """,
    'description': """
        The Mailing List Extended Module enhances the standard mailing list functionality by introducing advanced segmentation, subscription management, automation, and analytics features. This module is ideal for businesses that need precise control over their email marketing and audience targeting in Odoo.
    """,
    'author': "Infinys Odoo",
    'website': "https://www.infinyscloud.com/platform/odoo/",
    'category': 'Marketing/Email Marketing',
    'version': '0.1',
    'license': 'AGPL-3',
    'icon': '/infinys_mailinglist_contact/static/description/assets/infinyscloud.png',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mass_mailing',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mailing_contact_views.xml',
         'views/mailing_list_views.xml',   
  ],
     
'installable': True,
'application': False,
'auto_install': False,
 
}
