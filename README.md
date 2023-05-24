# H3_BigData

This is a big data module for installation in Odoo v16, this api retrives the latest data from weatherapi.com

## Installation
Upload the module to your odoo addons folder, and update the module list in Odoo and click activate

## Usage
Click on the menuitem "Big Data" in the menu list, and you will see all the data retrived from the weatherapi.com

To make changes or new cities, go to api settings to create or edit existing record.

### Warehousing
Go to the tap warehousing, and create new record with the necessary data, to be able to connect to the mongodb database/collection

When clicking on the "Update warehouse" button, Odoo will take a snapshot of the mongodb database, and import alle the data, and aggregate the date, and store it to the database, under the warehouse.

## Cron job
Every 10 minutes, a job will call the api, and checks on last updated, to not make duplicates.

## Tables 
- bigdata_api_data - This table stores the data from the api 
- bigdata_settings - Contains the api settings, and payload settings
- bigdata_warehouse - warehouse and mongodb settings
- bigdata_warehouse_line - warehouse data
- bigdata_dashboard - Dashboard and mongodb settigns
- bigdata_dashboard_line - Dashboard data

## Default Data
On install, the bigdata_settings table will be loaded with 20 records of settings for different cities to weatherapi.com

## Weatherapi.com
Data is updated ~15 min.

### v1
Cron job calls weatherapi.com every 10 minutes and prevents data redundency, because the api updates the data every ~15 min

### v2
Now supports warehousing and dashboarding / graphs