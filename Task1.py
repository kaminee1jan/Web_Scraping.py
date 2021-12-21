import requests
from bs4 import BeautifulSoup
import json
link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup=BeautifulSoup(link.text,"html.parser")
titles=soup.find_all("td", class_="unstyled articleLink")
def scrap_movie_list():
    maindiv=soup.find("div",class_="container")
    table= maindiv.find("div",class_="panel-body content_body allow-overflow")
    all_tr= table.find_all('tr')
    list1=[]
    for i in all_tr:
        all_td=i.find_all('td')
        dic={}
        for j in all_td:
            moviename=i.find("a",class_="unstyled articleLink")["href"][3:]
            rating=i.find("span",class_="tMeterScore").get_text()[:3]
            year=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            rank=i.find("td",class_="bold").get_text()
            reviews=i.find("td",class_="right hidden-xs").get_text()

            url=i.find("a",class_="unstyled articleLink")["href"]
            dic["Moviename"]=moviename
            dic["Rating"]=int(rating)
            dic["Year"]=year
            dic["Rank"]=rank
            dic["Reviews"]=reviews

            url_add= "https://www.rottentomatoes.com"+url
            dic["url"]=url_add
            list1.append(dic)
        with open("task1.json","w+") as movie_data:
            json.dump(list1,movie_data,indent=4)        
    return list1
movie_data=scrap_movie_list()

