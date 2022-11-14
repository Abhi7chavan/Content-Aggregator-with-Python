from django.shortcuts import render 
import requests
from bs4 import BeautifulSoup

Toi_r=requests.get('https://timesofindia.indiatimes.com/briefs')
Toi_soup=BeautifulSoup(Toi_r.content,"html.parser")

Toi_heading=Toi_soup.find_all('h2')
Toi_heading=Toi_heading[2:40] #removing Footers
Toi_news= []

for i in Toi_heading:
    Toi_news.append(i.text)

ht_r = requests.get("https://www.bbc.com/")
ht_soup = BeautifulSoup(ht_r.content, "html.parser")
ht_headings = ht_soup.find_all('h3')

ht_headings = ht_headings[:10]
bbc_news = []
for hth in ht_headings:
    bbc_news.append(hth.text)
india_r=requests.get('https://www.indiatoday.in/news.html')
india_sop=BeautifulSoup(india_r.content,"html.parser")
india_heading=india_sop.find_all('h3')
india_heading=india_heading[:10]
india_news=[]

for nt in india_heading:
    india_news.append(nt.text)


def home(request):
    return render(request,'home.html')
def bbc(request):
    return render(request,'BBC News.html',{'bbc_news':bbc_news})
def TOI(request):
    return render(request,'timesof.html',{'Toi_news':Toi_news})
def india(request):
    return render(request,'india.html',{'india_news':india_news})
