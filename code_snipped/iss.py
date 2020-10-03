import requests 

url = "http://api.open-notify.org/astros.json"
raw_data = requests.get(url).json()
# print(raw_data)

def humans_in_space(data: dict):
    # for (int p = 0; p < data.lenght; p++)
    humans = [p['name'] for p in data['people']]
    print(f'Сейчас в космосе: {data["number"]}')
    print(f'Сейчас на МКС находится {", ".join(humans)}')

humans_in_space(raw_data)