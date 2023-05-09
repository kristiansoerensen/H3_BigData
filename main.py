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