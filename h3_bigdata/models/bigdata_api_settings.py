from odoo import api, fields, models
import requests
import ast
import logging
from pymongo import MongoClient

_logger = logging.getLogger(__name__)

class BigDataAPISettings(models.Model):
    _name = 'bigdata.api.settings'
    _description = "Big Data API Settings"

    name = fields.Char("Name", required=True)
    base_url = fields.Char("Base Url", required=True)
    api_key = fields.Char("API Key", required=True)
    q = fields.Char("q")
    use_mongodb = fields.Boolean("Use MongoDB")
    mongodb_connection_str = fields.Char("MongoDB Connection string")
    mongodb_database = fields.Char("MongoDB Database")
    mongodb_collection = fields.Char("MongoDB Collection")

    # -------------
    # MongoDB
    # -----------
    
    def store_data_in_mongodb(self, response):
        with MongoClient(self.mongodb_connection_str) as cluster:
            db = cluster[self.mongodb_database]
            collection = db[self.mongodb_collection]
            try:
                data = ast.literal_eval(str(response.content.decode('utf-8')))
                mdb_response = collection.insert_one(data)
                _logger.info(f"Inserted data in mongoDB Object ID: {mdb_response.inserted_id}")
            except Exception as e:
                _logger.exception(e)
    
    # -------------
    # End MongoDB
    # ---------------

    def _request_data_from_api(self):
        uri = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.q}"
        _logger.info(uri)
        return requests.get(uri)

    def request_data_from_api(self, response):
        data = ast.literal_eval(str(response.content.decode('utf-8')))

        if not 'location' in data:
            _logger.warning(f"Location: {self.q}\n" + str(response.content.decode('utf-8')))
            return
        
        if self.env['bigdata.api.data'].search_count([
            ('last_updated', '=', data['current']['last_updated']), 
            ('name', '=', data['location']['name'])
            ]):
            return
        
        self.env['bigdata.api.data']._map_and_save_api_data(data)

    @api.model
    def _cron_call_api(self):
        for api in self.search([]):
            response = api._request_data_from_api()
            if api.use_mongodb:
                api.store_data_in_mongodb(response)
            else:
                api.request_data_from_api(response)