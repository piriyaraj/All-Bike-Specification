import re
import requests
from bs4 import BeautifulSoup
import os
url = "https://bikez.com/brands/index.php"


def exractModelsLink(url):
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
        if(i.findAll("td")[1].text==""):
            # print("==>"+i.findAll("td")[0].text)
            continue
        atag=i.findAll("a")[0]

        link_m="https://bikez.com/"+atag.get_attribute_list("href")[0].split("../")[1]
        links.append(link_m)

    return links

def filemake(name):
    try:
        file=open(name,"r+")
    except:
        open(name,"w").close()
        file=open(name,"r+")
    return file

def expandUrlpost(url):
    post_links = []
    try:
        reqs = requests.get(url)
    except:
        print("Check Internet connection !")
        return []
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table=soup.find_all('table')[2]
    tr=table.find_all('tr')
    # print(tr)
    for i in tr:
        if(tr.index(i)==0):
            continue
        tdTags = i.findAll('td')
        if(len(tdTags)>2 or len(tdTags[0].findAll('img'))==0):
            continue
        
        t=i.findAll('td')[1].findAll('a')
        for i in t:
            if(i.get_attribute_list('href')[0]==None):
                continue
            else:
                link="https://bikez.com"+i.get_attribute_list("href")[0].split("..")[1]
        post_links.append(link)
    return post_links

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
    # print(tr)
    for i in tr:
        if(tr.index(i)==0):
            continue
        expandTag = i.findAll('td')[0].findAll('a')
        if(len(expandTag)!=0):
            expandUrl=url+expandTag[0].get_attribute_list('href')[0]
            expandpostUrls = expandUrlpost(expandUrl)
            post_links=post_links+expandpostUrls
            continue
        
        t=i.findAll('td')[1].findAll('a')
        for i in t:
            if(i.get_attribute_list('href')[0]==None):
                continue
            else:
                link="https://bikez.com"+i.get_attribute_list("href")[0].split("..")[1]
        post_links.append(link)
    return post_links



def run():
    try:
        os.makedirs("data/models")
    except:pass
    global url

    fileModlelinks = filemake("./data/models/modelsLinks.txt")

    filetopost=filemake("./data/topost.txt")
    modelsLinks=exractModelsLink(url)
    for modelLink in modelsLinks:

        modelforfile = modelLink.split("models/")[1].split(".")[0]
        # try:
        #     if(yearforfile.index("=")):
        #         yearforfile=yearforfile.split("=")[1]
        # except:pass
        print("\n\n>>> "+modelforfile,end="")

        postlinks = exractpostlink(modelLink)
        print(" ||| NO of Post: ",len(postlinks))
        fileModel = filemake("./data/models/"+modelforfile+".txt")
        links = fileModel.readlines()
        for postlink in postlinks:
            try:
                pos=links.index(postlink+"\n")
            except:pos=-1
            if(pos==-1):

                filetopost.write(postlink+"\n")
                fileModel.write(postlink+"\n")
                print("======>>>"+postlink)

        fileModlelinks.write(modelLink+"\n")
        fileModel.close()

    fileModlelinks.close()
    filetopost.close()


#postlinks_n="https://bikez.com/year/2020-motorcycle-models.php"
#linkss=exractpostlink(postlinks_n)
if __name__ == "__main__":
    # run()

    # postLinks = exractpostlink("https://bikez.com/models/ajs_models.php")
    # print(len(postLinks))

    # expandpostUrls = expandUrlpost(
    #     "https://bikez.com/models/access_models.php?expser=2784#explist")
    # print(expandpostUrls)
    run()
    pass
