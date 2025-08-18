from requests import get
from time import sleep


def get_top_ids():
    # トップ記事一覧のid取得
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = get(url, params="print=pretty")
    news_ids = response.json()

    return news_ids


if __name__ == "__main__":

    # 各記事のidをurlに当てはめる
    for i in range(30):
        sleep(1)

        id = get_top_ids()
        article = f"https://hacker-news.firebaseio.com/v0/item/{id[i]}.json"
        response = get(article)
        news_data = response.json()

        print(f"title: {news_data["title"]}, link: {news_data["url"]}")
