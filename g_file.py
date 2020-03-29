import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
import pandas
nltk.download('punkt')

def details(url,wrd):
    d={}
    obj=Article(url)
    obj.download()
    obj.parse()
    obj.nlp()
    d["Title"] = obj.title
    d["Publish Date"] = obj.publish_date
    d["Summarized text"] = obj.summary   
    d["URL"] = url
    text = obj.text
    text = text.split('.')
    for i in text:
        if wrd in i:
            print(i)
    return d

#%%
url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class":"xrnccd F6Welf R7GTQ keNKEd j7vNaf"})

wrd = input("Enter search word:")

#%%
l1=[]
c=0
for i in all:
    c+=1
    x1 = i.find("h3").find("a").get('href')
    x2 = "https://news.google.com"+x1[1:]
    l1.append(details(x2))
    y = i.find_all("h4")
    l2=[]
    for j in y:
        z1 = j.find("a").get('href')
        z2 = "https://news.google.com"+z1[1:]
        l2.append(details(z2))
    df_sub = pandas.DataFrame(l2)
    df_sub.to_csv("Sub News %s.csv" %c)        
    
df_main = pandas.DataFrame(l1)
df_main.to_csv("Main News.csv")