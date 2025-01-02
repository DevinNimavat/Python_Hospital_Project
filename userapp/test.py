import requests


def get_api():
    url = 'https://raw.githubusercontent.com/sab99r/Indian-States-And-Districts/refs/heads/master/states-and-districts.json'
    req = requests.get(url)
    data = req.json()
    state=data['states']
    for i in state:
        print(i['state'])
        print(i['districts'])

get_api()