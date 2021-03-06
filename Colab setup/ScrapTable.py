import json
import re
import requests
from bs4 import BeautifulSoup
import articalWriter
def getdata(url):

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    tableArtical={}
    for i in soup.find_all('table'):
        if(i.text.find("General information")!=-1 or i.text.find("General moped information")!=-1 or i.text.find("Other specifications")!=-1):
            table=i
            break
    # find title of the post
    title=soup.title.text
    tags=title.split()[1]+","+title.split()[0]
    catecary = title.split()[1]
    if(title.find("|")>0):
        # print("loop",title)
        tags = title.split()[0]+","+title.split("|")[1].replace(" ", "")
        catecary = title.split()[0]
        title=title.split()[0]+" "+title.split()[0]+" "+title
        # print("loop",title)

    title=title.replace(" specifications and pictures","").replace(title.split()[0]+" ","")+" | Price, Photos, Millage, Speed, Colours etc."

    if(title.find(tags.split(",")[0])<0):
        title=tags.split(",")[0]+" "+title
    # print("loop",title)

    title = title.split(" |")[0]+" "+tags.split(",")[1]

    # find the table date of the post
    trTags=table.findAll("tr")
    allKeys=[]
    allData={}
    keyValue = {}
    for i in trTags:
        tdTags=i.findAll("td")
        if(len(tdTags)==0):
            tableName=i.text
            # print(keyValue)
            if(len(keyValue)>0):
                allData[tableName] = keyValue
                artical = articalWriter.maker1(keyValue, tableName)
                if(artical!=""):
                    tableArtical[tableName] = artical
            keyValue={}
            allKeys.sort()
            # allKeys=print(allKeys)
            allKeys=[]
            
            

        if(len(tdTags)==2):
            key = re.sub(r'[^\w]', ' ', tdTags[0].text)
            key = key.strip()
            keyValue[key] =tdTags[1].text
            allKeys.append(key)
    allData["artical"]=tableArtical
    # print(json.dumps(allData,indent=4))
    # print(tableArtical)
    return title, catecary, allData


if __name__=="__main__":
    url="https://bikez.com/motorcycles/access_ams_320_supercross_2016.php"
    url1="https://bikez.com/motorcycles/arctic_cat_alterra_570_eps_se_2021.php"
    url2="https://bikez.com/motorcycles/bmw_r_ninet_2021.php"
    url3 = "https://bikez.com/motorcycles/acabion_da_vinci_650-vi_2011.php"
    # #
    getdata(url3)
