# H3_BigData

This is a big data module for installation in Odoo v16

## Installation
Upload the module to your odoo addons folder, and update the module list in Odoo and click activate

## Usage
Click on the menuitem "Big Data" in the menu list, and you will see all the data retrived from the weatherapi.com

To make changes or new cities, go to api settings to create or edit existing record.

## Cron job
Every 10 minutes, a job will call the api, and checks on last updated, to not make duplicates.

## Tables 
- bigdata_api_data - This table stores the data from the api 
- bigdata_settings - Contains the api settings, and payload settings

## Default Data
On install, the bigdata_settings table will be loaded with 20 records of settings for different cities to weatherapi.com

## Weatherapi.com
Data is updated ~15 min.