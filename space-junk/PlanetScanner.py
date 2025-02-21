import requests

class PlanetScanner:
    
    def scan(self, coord1: int = 41.6414, coord2: int = 80.1514):
        data = requests.get(
            "https://api.openweathermap.org/data/2.5/weather/",
            params = {
                "lat": coord1,
                "lon": coord2,
                "appid": "e94e7399d7722cc93a701ca0e6f5fe78"
            }
        )
        return list(
            data.json()['main'].values()
        )[0]

result = PlanetScanner().scan()
