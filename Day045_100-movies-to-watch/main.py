import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
FILENAME = "top-movies.txt"

def write_to_file(filename, content):
    with open(filename, "w", encoding="utf8") as file_movies:
        for line in content[::-1]:
            file_movies.write(str(line) + "\n")

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
best_movies_article = soup.select("span.content_content__i0P3p h2 strong")
    # --> This returns array: [<strong>100) Reservoir Dogs (1992)</strong>, <strong>99) Groundhog Day (1993)</strong>,...]
best_movies_article = [movie.text for movie in best_movies_article]
print(best_movies_article)

write_to_file(FILENAME, best_movies_article)


##
# Source Path and Pattern:
# Pattern:
# Path:
#   html body.empire div#__next main article.article_content__HfTvf div.article_article-content__3auQJ.false span.content_content__i0P3p h2 strong
#   Xpath: /html/body/div/main/article/div[3]/span[8]/h2/strong

