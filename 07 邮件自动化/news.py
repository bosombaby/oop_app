import requests
from pprint import pprint


class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = '2969e654927c4df08fe4d89db0fb5870'

    def __init__(self, interest, from_date, to_date, language='zh'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self.__build_url()
        articles = self.__get_result(url)
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n'

        return email_body

    def __get_result(self, url):
        result = requests.get(url)
        content = result.json()
        articles = content['articles']
        return articles

    def __build_url(self):
        url = f'{self.base_url}' \
              f'q={self.interest}&' \
              f'searchIn=title&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}' \
              f'sortBy=publishedAt&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'

        return url


if __name__ == '__main__':
    news = NewsFeed('航天', '2023-07-2', '2023-07-28', 'zh')
    print(news.get())
