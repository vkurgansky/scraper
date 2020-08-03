import requests
from common import log


class Scraper:
    @staticmethod
    def get_content_in_html(url):
        log(f"Getting response from '{url}'...")
        r = requests.get(url)
        return r.text
