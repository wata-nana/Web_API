from requests import get
from time import sleep


def get_top_ids():
    # トップ記事一覧のid取得
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = get(url, params="print=pretty")
    news_ids = response.json()

    return news_ids


def get_top_articles():
    # 各記事のidをurlに当てはめる
    for i in range(30):
        sleep(1)

        id = get_top_ids()
        article = f"https://hacker-news.firebaseio.com/v0/item/{id[i]}.json"
        response = get(article)
        news_data = response.json()

        if ("title" and "url") in news_data:
            article_box = {"title": news_data["title"], "link": news_data["url"]}
            print(article_box)
        else:
            pass


if __name__ == "__main__":
    get_top_articles()
