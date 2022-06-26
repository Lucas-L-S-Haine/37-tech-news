import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url, timeout=3):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    time.sleep(1)
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    selector_list = " ".join([
        "article",
        ".post-outer",
        ".post-inner",
        ".entry-header",
        ".entry-title",
        "a::attr(href)",
    ])
    result = selector.css(f"{selector_list}").getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
