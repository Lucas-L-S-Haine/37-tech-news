from tech_news.database import db


# Requisito 6
def search_by_title(title):
    query = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"_id": False, "title": True, "url": True})
    news_list = list(query)
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    query = db.news.find(
        {"tags": {"$regex": tag, "$options": "i"}},
        {"_id": False, "title": True, "url": True})
    news_list = list(query)
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))
    return result


# Requisito 9
def search_by_category(category):
    query = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"_id": False, "title": True, "url": True})
    news_list = list(query)
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))
    return result
