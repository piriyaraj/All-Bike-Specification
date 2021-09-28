import re
# from sys import ps1
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup, dammit
from firebase import firebase
import pyrebase
from requests.models import ReadTimeoutError
from firebase import firebase

totalPhotos = 0
databaseUrl = "https://colabfacebook-default-rtdb.firebaseio.com/Website/AllBikeSpecification/"
# databaseUrl = "https://colabfacebook-default-rtdb.firebaseio.com/"
dataBase = firebase.FirebaseApplication(databaseUrl, None)
# mainSitemapUrl = "https://www.whatsapgrouplinks.com/sitemap_index.xml"
# read firebase data


def readFirebaseDate(tableName):
    dataValueList=[]
    ResultSet = dataBase.get(databaseUrl, tableName,)
    try:
        for i in(list(ResultSet.values())):
            dataValueList.append(i['url'])
        return dataValueList
    except:
        return 0

# insert data into firebase

# toPostList=[]
noOfPost = 2
def insertData(tableName, data, dataBase, format="post"):
    if(format == "patch"):
        result = dataBase.patch(tableName, data)
    else:
        result = dataBase.post(tableName, data)


def initialize():
    dataSet = dataBase.get(databaseUrl, 'data/posted',)
    toPostList = list(dataSet.keys())[:noOfPost]
    return toPostList
    # print(toPostList)

# delete first line


def delete(bikeName):
    return dataBase.delete(databaseUrl, 'data/posted/'+bikeName)

# last post link


def posted(title, posted_link):
    insertData('data/postedInBlogger', {title: posted_link},dataBase, format='patch')


def run():
    pass
    
if __name__=="__main__":
    # insertData('data/models/'+"acabion_models",{"url": "https://bikez.com/motorcycles/acabion_da_vinci_650-vi_2011.php"}, dataBase)
    # insertData('data/models/'+"acabion_models",{"url": "https://bikez.com/motorcycles/acabion_gtbo_600_daytona-vi_2021.php"}, dataBase)
    # links = readFirebaseDate('data/models/'+"acabion_models")

    # insert topost 
    # insertData('data/topost',{"url": "https://bikez.com/motorcycles/acabion_gtbo_600_daytona-vi_2021.php"}, dataBase)
    # toPostList=initialize()
    print(posted("a", "posted"))
    # print(delete(toPostList[0]))

    # print(links)
