import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select(".titleline")
articles = [article.select_one("a") for article in articles]
article_scores = soup.select(".score")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# print(article_text)
# print(article_link)
article_titles = [article.text for article in articles]
article_hrefs = [article.get("href") for article in articles]
article_scores = [int(score.text.split(" ")[0]) for score in article_scores]

print(articles)
print(article_titles)
print(article_hrefs)
print(article_scores)


highest_score_index = article_scores.index(max(article_scores))
print(highest_score_index)
print(article_titles[highest_score_index])
print(article_hrefs[highest_score_index])

