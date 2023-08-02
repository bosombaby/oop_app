import requests
from selectorlib import Extractor


class Temperature:
    base_url = "https://www.timeanddate.com/weather/"

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def __build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    def __scrape(self):
        url = self.__build_url()
        extractor = Extractor.from_yaml_file("temperature.yaml")
        res = requests.get(url).text
        raw_content = extractor.extract(res)
        return raw_content

    def get(self):
        scrape_content = self.__scrape()
        result = scrape_content["weather"].replace("\xa0°C", "")
        return float(result)


if __name__ == "__main__":
    temp = Temperature("usa", "new-york")
    print(temp.get())
