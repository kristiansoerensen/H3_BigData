from odoo import models, fields, api, _
from datetime import datetime, timedelta
from pymongo import MongoClient
import logging

_logger = logging.getLogger(__name__)

class BigDataDashboard(models.Model):
    _name = 'bigdata.dashboard'
    _description = 'Big Data Dashboard'

    name = fields.Char("Name")
    mongodb_connection_str = fields.Char("MongoDB Connection string")
    mongodb_database = fields.Char("MongoDB Database")
    mongodb_collection = fields.Char("MongoDB Collection")

    data_count = fields.Integer("Data count", compute="_compute_data_count")

    def action_open_data_lines(self):
        return {
            'name': _("Dashobard data"),
            'type': 'ir.actions.act_window',
            'res_model': 'bigdata.warehouse.line',
            'context': {'create': False},
            'domain': [('dashboard_id', '=', self.id)],
            'view_mode': 'list,form',
        }
    
    def _compute_data_count(self):
        for record in self:
            record.data_count = self.env['bigdata.dashboard.line'].search_count([('dashboard_id', '=', record.id)])

    def action_populate_dashboard(self):
        # Unlink all reords older then 24 hours
        find_after_datetime = datetime.now() + timedelta(days = -1)
        self.env['bigdata.dashboard.line'].search([
            ('last_updated', '<=', find_after_datetime),
            ('dashboard_id', '=', self.id)
            ]).unlink()

        # Populate with new data
        with MongoClient(self.mongodb_connection_str) as cluster:
            db = cluster[self.mongodb_database]
            collection = db[self.mongodb_collection]
            cursor = collection.find().limit(100).sort("{$natural:-1}") 
            _logger.info("cu3efsddsfsfsrsor")
            for document in cursor:
                _logger.info("cursor")
                self.env['bigdata.dashboard.line']._map_and_save_mongodb_document(document, self)

    
    @api.model
    def _cron_populate_dashboards(self):
        for dasboard in self.search([]):
            dasboard.action_populate_dashboard()
    
    def action_open_data_lines(self):
        pass