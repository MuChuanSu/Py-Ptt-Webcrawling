import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url = "https://www.ptt.cc/bbs/nba/index.html"

#1. get response and make it a soup
response = requests.get(url)
text = response.text
soup = BeautifulSoup(text,features="html.parser")

#find where are the info we need in the html file
#in this case we need the articles title,popularity and date
#the articles are all in the "div" class with a "r-ent" class
#2.find all the div class with soup.find(), it will return a list

articles = soup.findAll("div",class_ = "r-ent")


#now we've got the articles in a list, we can use a for loop to extract the info
#3.and put them into a dictuinary and into a list


dicList = []

for i in articles:
    pttDic={}
    if i.find("div",class_="title").a is not None:
        title = i.find("div",class_="title").a.text
        articleUrl ="ptt.cc"+(i.find("div",class_="title").a.get('href'))


    else:
        title= i.find("div",class_="title").text
        articleUrl ="N/A"

    popularity = i.find("div",class_="nrec").text
    date = i.find("div",class_= "date").text

    pttDic["Title"] = title
    pttDic["Popularity"] = popularity
    pttDic["Date"] = date
    pttDic["Url"] = articleUrl
    dicList.append(pttDic)


#4. we have stored the data into the dictionary and a list,we can use pandas to put it into xsl file

df = pd.DataFrame(dicList)
df.to_excel("NBA.xlsx",index=False,engine="openpyxl")





