from odoo import api, fields, models, _
import requests
import ast
from pymongo import MongoClient
import logging

_logger = logging.getLogger(__name__)

class BigDataWarehouse(models.Model):
    _name = 'bigdata.warehouse'
    _description = "Big Data warehouses"

    name = fields.Char("Name")
    line_ids = fields.One2many("bigdata.warehouse.line", "warehouse_id", string="Data lines")
    mongodb_connection_str = fields.Char("MongoDB Connection string")
    mongodb_database = fields.Char("MongoDB Database")
    mongodb_collection = fields.Char("MongoDB Collection")

    data_count = fields.Integer("Data count", compute="_compute_data_count")

    def action_open_data_lines(self):
        return {
            'name': _("Warehouse data"),
            'type': 'ir.actions.act_window',
            'res_model': 'bigdata.warehouse.line',
            'context': {'create': False, 'search_default_warehouse_id': self.id},
            'view_mode': 'list,form',
        }
    
    def _compute_data_count(self):
        for record in self:
            record.data_count = self.env['bigdata.warehouse.line'].search_count([('warehouse_id', '=', record.id)])

    def action_populate_warehouse(self):
        # Delete already existing records!
        self.env['bigdata.warehouse.line'].search([('warehouse_id', '=', self.id)]).unlink()

        # Populate with new data
        with MongoClient(self.mongodb_connection_str) as cluster:
            db = cluster[self.mongodb_database]
            collection = db[self.mongodb_collection]
            cursor = collection.find({})
            for document in cursor:
                self.env['bigdata.warehouse.line']._map_and_save_mongodb_document(document, self)
