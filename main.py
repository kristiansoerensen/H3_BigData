import requests
import ast

cities = ['Sonderborg', 'Graasten', 'Kvaers', 
        'Dybbol', 'Nordborg', 'Augustenborg', 
        'Horuphav', 'Guderup', 'Ergensund', 
        'Nybol', 'Fynshav', 'Blans', 'Tanslet',
        'Svenstrup', 'Skovby', 'Avnbol', 'Hundslev',
        'Holm', 'Ullerup', 'Adsbol', 'Skelde', 'Stevning'
        ]

for city in cities:
    
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=5e2d49dc7d054aca93a114602230905&q={city}")
    # print(response.content)
    print(ast.literal_eval(str(response.content.decode('utf-8'))))

"""
{
    'location': 
        {
                'name': 'Stevning', 
                'region': 'Syddanmark', 
                'country': 'Denmark', 
                'lat': 55.02, 
                'lon': 9.83, 
                'tz_id': 'Europe/Copenhagen', 
                'localtime_epoch': 1683710254, 
                'localtime': '2023-05-10 11:17'
        }, 
        'current': 
                {
                'last_updated_epoch': 1683709200, 
                'last_updated': '2023-05-10 11:00', 
                'temp_c': 13.0, 
                'temp_f': 55.4, 
                'is_day': 1, 
                'condition': 
                        {
                            'text': 'Sunny', 
                            'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 
                            'code': 1000
                        }, 
                'wind_mph': 18.6, 
                'wind_kph': 29.9, 
                'wind_degree': 130, 
                'wind_dir': 'SE', 
                'pressure_mb': 1009.0, 
                'pressure_in': 29.8, 
                'precip_mm': 0.0, 
                'precip_in': 0.0, 
                'humidity': 67, 
                'cloud': 0, 
                'feelslike_c': 10.7, 
                'feelslike_f': 51.3, 
                'vis_km': 10.0, 
                'vis_miles': 6.0, 
                'uv': 4.0, 
                'gust_mph': 20.1, 
                'gust_kph': 32.4
                }
        }
}
"""