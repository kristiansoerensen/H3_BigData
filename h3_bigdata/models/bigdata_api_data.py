from odoo import api, fields, models

class BigDataAPISettings(models.Model):
    _name = 'bigdata.api.data'
    _description = "Big Data API Data"
    _order = "name"

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