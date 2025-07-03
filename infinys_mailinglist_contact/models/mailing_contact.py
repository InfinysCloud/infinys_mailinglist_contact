import logging
import datetime
import requests
from datetime import timedelta
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class MailingContact(models.Model):
    """This class is used to inherit users and add api key generation"""
    _inherit = 'mailing.contact'

    job_position = fields.Char(string="Job Position",
                                  help="Job position of the contact, eg. Sales Director")
    phone = fields.Char(string="Phone",
                        help="Phone number of the contact, eg. +62 21234 567 890")
    mobile = fields.Char(string="Mobile",
                         help="Mobile number of the contact, eg. +62 812 3456 7890")
    website = fields.Char(string="Website",
                          help="Website of the contact, eg. https://www.example.com")

    
    state_id = fields.Many2one('res.country.state')
    city = fields.Char()
    
    postcode = fields.Char("ZIP")
   
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if (
            self.country_id
            and self.state_id
            and self.state_id not in self.country_id.state_ids
        ):
            self.state_id = False

    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            self.country_id = self.state_id.country_id.id

   