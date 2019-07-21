# -*- coding: utf-8 -*-
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print soup.prettify()


from bs4 import BeautifulSoup
import urllib2

redditFile = urllib2.urlopen("http://www.126.com")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml,"html.parser")

print soup.title.string
print soup.title.name
soup.title.string = "1222"


redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print  links.get_text(), links.get('href')
    links.replace_with("ccc")
    print links.get_text()