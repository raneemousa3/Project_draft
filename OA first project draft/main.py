from bs4 import BeautifulSoup
import requests
html_text=requests.get('https://www.teenlife.com/category/summer/?keyword=python&program-type=summer').text

soup=BeautifulSoup(html_text,'html.parser')



"""summer_programs=soup.find('section', class_ ='cat-content')
content=summer_programs.find('div',class_ = 'wrapper')
text=content.find('p').span.text
print(text)"""


summer_programs=soup.find('div', class_ ="right-search-area main-category-search-area")
#h3=soup.select("article")
closer=summer_programs.find('div', class_ ="loader-matchprgm-container")  
article=closer.find('div', class_ ="matched-programs no-bg")
title=article.find('article', class_ ="featured")
print(title)

#program_name=summer_programs.find('h3',class_="program-heading featured")['href']
#print(summer_programs)
