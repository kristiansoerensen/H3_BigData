from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class BigDataWarehouseLine(models.Model):
    _name = 'bigdata.warehouse.line'
    _description = "Big Data warehouse lines"
    _order = "last_updated"

    warehouse_id = fields.Many2one("bigdata.warehouse", string="Warehouse", required=True, ondelete="cascade")

    name = fields.Char("Name")
    region = fields.Char("Region")
    country = fields.Char("Country")
    lat = fields.Float("Latitude")
    lon = fields.Float("Longitude")
    tz_id = fields.Char("Time zone")
    last_updated = fields.Datetime("Last Updated")
    temp_c = fields.Float("Tempature C", group_operator='avg')
    is_day = fields.Boolean("Is day")
    condition = fields.Char("Sunny")
    wind_kph = fields.Float("Wind kph", group_operator='avg')
    wind_degree = fields.Float("Wind degree", group_operator='avg')
    wind_dir = fields.Char("Wind Direction")
    pressure_mb = fields.Float("Pressure MB", group_operator='avg')
    precip_mm = fields.Float("Precip MM", group_operator='avg')
    humidity = fields.Integer("Humidity", group_operator='avg')
    cloud = fields.Boolean("Cloud")
    feelslike_c = fields.Float("Feelslike C", group_operator='avg')
    vis_km = fields.Float("Visabillity Km", group_operator='avg')
    uv = fields.Float("UV", group_operator='avg')
    gust_kph = fields.Float("Gust kph")

    @api.model
    def _map_and_save_mongodb_document(self, data, warehouse_id):
        if not 'location' in data:
            _logger.error(f"Error data: {data}")
            return
        
        if self.env['bigdata.warehouse.line'].search_count([
            ('warehouse_id', '=', warehouse_id.id),
            ('last_updated', '=', data['current']['last_updated']), 
            ('name', '=', data['location']['name'])
            ]):
            _logger.info("Skipping record, does already exist!")
            return

        record = self.env['bigdata.warehouse.line'].create({
            'warehouse_id': warehouse_id.id,
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