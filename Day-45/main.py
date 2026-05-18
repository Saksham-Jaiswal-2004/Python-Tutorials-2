from bs4 import BeautifulSoup
import requests

with open("website.html") as file:
    contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find_all(name="h1", id="name")
# print(heading[0].getText())

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
TitleSpan = soup.find_all(name="span", class_="titleline")
ScoreSpan = soup.find_all(name="span", class_="score")

article_title_list = []
article_link_list = []

for article in TitleSpan:
    article_title_list.append(article.find('a').getText())
    article_link_list.append(article.find('a').get("href"))

article_upvote_list = [int(score.getText().split()[0]) for score in ScoreSpan]

print(article_title_list)
print(article_link_list)
print(article_upvote_list)

max_index = article_upvote_list.index(max(article_upvote_list))
print("\n")
print(article_title_list[max_index])
print(article_link_list[max_index])
print(article_upvote_list[max_index])