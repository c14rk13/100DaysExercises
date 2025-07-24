from bs4 import BeautifulSoup
#import lxml -- if html.parser cannot properly parse website

with open("./website.html") as the_website:
    contents = the_website.read()

soup = BeautifulSoup(contents,"html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())
print(soup.a) # first <a> tag
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
     print(tag.getText())
     print(tag.get("href")) #get the value of the given attribute name

heading =soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
    # Look for <a> tag that sits under a <p> tag
print(company_url)
name = soup.select_one(selector="#name")
    # Look for element with id = name
print(name)

headings = soup.select(".heading") #select element/s with class = heading
print(headings)
