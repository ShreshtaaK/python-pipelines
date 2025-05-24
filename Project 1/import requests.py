import requests
import json

countries = ['india', 'us', 'uk', 'china', 'russia']
base_url = 'https://restcountries.com/v3.1/name/'

for country in countries:
    try:
        url = base_url + country
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        filename = f"{country.lower()}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Data for {country} saved to {filename}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error for {country}: {err}")
    except Exception as e:
        print(f"Error fetching data for {country}: {e}")
