import re
import requests
from bs4 import BeautifulSoup
import os
url="https://bikez.com/years/index.php"


def exractyearlink(url):
    try:
        reqs = requests.get(url)
    except:
        print("check internet connection !")
        return []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table=soup.findAll('table',class_="zebra")[0]
    trs=table.findAll("tr")
    links=[]
    for i in trs[1:]:
        atag=i.findAll("a")[0]

        link_y="https://bikez.com/"+atag.get_attribute_list("href")[0].split("../")[1]
        links.append(link_y)

    return links

def filemake(name):
    try:
        file=open(name,"r+")
    except:
        open(name,"w").close()
        file=open(name,"r+")
    return file

def exractpostlink(url):
    post_links=[]
    try:
        reqs = requests.get(url)
    except:
        print("Check Internet connection !")
        return []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table=soup.find_all('table')[2]
    tr=table.find_all('tr')
    for i in tr:
        if(tr.index(i)==0):
            continue
        if(len(i.findAll('td'))==3):
            linktag=i.findAll('td')[0]
        elif(len(i.findAll('td'))==2):
            linktag=i.findAll('td')[1]
        else:
            continue
        t=linktag.findAll('a')
        for i in t:
            if(i.get_attribute_list('href')[0]==None):
                continue
            else:
                link="https://bikez.com"+i.get_attribute_list("href")[0].split("..")[1]
        post_links.append(link)
    return post_links



def run():
    try:os.makedirs("data/years")
    except:pass
    global url

    fileyearlinks=filemake("./data/years/yearlinks.txt")

    filetopost=filemake("./data/topost.txt")
    year_links=exractyearlink(url)
    for i in year_links:
        yearllink=i

        yearforfile=yearllink.split("year/")[1].split("-")[0]
        try:
            if(yearforfile.index("=")):
                yearforfile=yearforfile.split("=")[1]
        except:pass
        print(yearforfile)


        postlinks=exractpostlink(yearllink)


        fileyear=filemake("./data/years/"+yearforfile+".txt")
        links=fileyear.readlines()
        for postlink in postlinks:
            try:
                pos=links.index(postlink+"\n")
            except:pos=-1
            if(pos==-1):

                filetopost.write(postlink+"\n")
                fileyear.write(postlink+"\n")

        fileyearlinks.write(yearllink+"\n")
        fileyear.close()

    fileyearlinks.close()
    filetopost.close()


#postlinks_n="https://bikez.com/year/2020-motorcycle-models.php"
#linkss=exractpostlink(postlinks_n)
