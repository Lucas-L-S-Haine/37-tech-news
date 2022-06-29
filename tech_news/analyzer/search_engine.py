import datetime

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
def translate_month(month):
    month_br = {
        "January": "janeiro",
        "February": "fevereiro",
        "March": "março",
        "April": "abril",
        "May": "maio",
        "June": "junho",
        "July": "julho",
        "August": "agosto",
        "September": "setembro",
        "October": "outubro",
        "November": "novembro",
        "December": "dezembro",
    }
    try:
        result = month_br[month]
    except KeyError:
        result = month
    return result


def validate_date(date_str):
    try:
        date = datetime.date.fromisoformat(date_str)
    except ValueError:
        raise(ValueError("Data inválida"))
    return date


def search_by_date(date):
    if not validate_date(date):
        raise(ValueError("Data inválida"))
    month = datetime.date.fromisoformat(date).strftime("%B")
    month_br = translate_month(month)
    day = datetime.date.fromisoformat(date).strftime("%d").removeprefix("0")
    year = datetime.date.fromisoformat(date).strftime("%Y")
    search_date = f"{day} de {month_br} de {year}"
    query = db.news.find(
        {"timestamp": search_date},
        {"_id": False, "title": True, "url": True})
    news_list = list(query)
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))
    print("\n", date)
    print("\n", result)
    return result


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
