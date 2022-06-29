import time
from math import floor, ceil
import requests
from parsel import Selector

from tech_news.database import create_news


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
    selector = Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    title = selector.css("h1.entry-title::text").get()
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    category = selector.css("a.category-style span.label::text").get()
    author = selector.css("a.url.fn.n::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    tags = selector.css("section.post-tags ul li a::text").getall()
    summary_selector = "div.entry-content p:nth-child(2) ::text"
    summary = "".join(selector.css(summary_selector).getall())
    data = {
        "title": title,
        "url": url,
        "category": category,
        "comments_count": 0,
        "writer": author,
        "timestamp": timestamp,
        "tags": tags,
        "summary": summary,
    }
    return data


# Requisito 5
def get_url_list(amount):
    base_url = "https://blog.betrybe.com/"
    next_page_url = base_url
    links_list = []
    while len(links_list) <= amount:
        html_content = fetch(next_page_url)
        links = scrape_novidades(html_content)
        next_page_url = scrape_next_page_link(html_content)
        links_list.extend(links)
    result = links_list[0:amount]
    return result


def get_scrape_noticia(url_list):
    news_info_list = []
    for url in url_list:
        html_content = fetch(url)
        news_info = scrape_noticia(html_content)
        news_info_list.append(news_info)
    return news_info_list


def get_tech_news(amount):
    url_list = get_url_list(amount)
    result = get_scrape_noticia(url_list)
    create_news(result)
    return result
