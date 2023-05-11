from odoo import api, fields, models
import requests
import ast
import logging

_logger = logging.getLogger(__name__)

class BigDataAPISettings(models.Model):
    _name = 'bigdata.api.settings'
    _description = "Big Data API Settings"

    name = fields.Char("Name", required=True)
    base_url = fields.Char("Base Url", required=True)
    api_key = fields.Char("API Key", required=True)
    q = fields.Char("q")

    def request_data_from_api(self):
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.q}")
        data = ast.literal_eval(str(response.content.decode('utf-8')))

        if not 'location' in data:
            _logger.warning(f"Location: {self.q}\n" + str(response.content.decode('utf-8')))
            return
        
        if self.env['bigdata.api.data'].search_count([
            ('last_updated', '=', data['current']['last_updated']), 
            ('name', '=', data['location']['name'])
            ]):
            return

        record = self.env['bigdata.api.data'].create({
            'name': data['location']['name'],
            'region': data['location']['region'],
            'country': data['location']['country'],
            'lat': data['location']['lat'],
            'lon': data['location']['lon'],
            'tz_id': data['location']['tz_id'],
            'last_updated': data['current']['last_updated'],
            'temp_c': data['current']['temp_c'],
            'is_day': data['current']['is_day'],
            'condition': data['current']['condition']['text'],
            'wind_kph': data['current']['wind_kph'],
            'wind_degree': data['current']['wind_degree'],
            'wind_dir': data['current']['wind_dir'],
            'pressure_mb': data['current']['pressure_mb'],
            'precip_mm': data['current']['precip_mm'],
            'humidity': data['current']['humidity'],
            'cloud': data['current']['cloud'],
            'feelslike_c': data['current']['feelslike_c'],
            'vis_km': data['current']['vis_km'],
            'uv': data['current']['uv'],
            'gust_kph': data['current']['gust_kph'],
        })

        _logger.info(f"record created {record.id}")

    @api.model
    def _cron_call_api(self):
        for api in self.search([]):
            api.request_data_from_api()