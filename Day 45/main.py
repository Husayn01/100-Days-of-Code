from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)
anchor_tag = soup.select_one(selector="span a")
print(anchor_tag.getText())

#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)
# # print(soup)
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# for item in all_anchor_tags:
#     print(item)
#     print(item.get_text())
#     print(item.get("href"))
#
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# company_url = soup.select_one(selector="p a")
# print(heading)
# print(section_heading)
# print(company_url)