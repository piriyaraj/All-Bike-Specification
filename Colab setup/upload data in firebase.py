import os
import sys

from requests.api import patch
import ScrapTable
import re
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup, dammit
from firebase import firebase
import pyrebase
from requests.models import ReadTimeoutError
from firebase import firebase
import urlexract


databaseUrl = "https://all-bike-specification-default-rtdb.firebaseio.com/"

databaseUrlColab = "https://colabfacebook-default-rtdb.firebaseio.com/Website/AllBikeSpecification/"
dataBaseColab = firebase.FirebaseApplication(databaseUrlColab, None)


noOfPost=1


accNO=0
if(len(sys.argv)>1):
    accNO=int(sys.argv[1])



def insertData(tableName, data, dataBase, format="post"):
    if(format == "patch"):
        result = dataBase.patch(tableName, data)
    else:
        result = dataBase.post(tableName, data)



def initialize():
    dataSet = dataBaseColab.get(databaseUrlColab, 'data/topost',)
    toPostList = list(dataSet.keys())[:noOfPost]
    return toPostList
    # print(toPostList)

# read first line
def read(id):
    postLink = dataBaseColab.get(databaseUrlColab, 'data/topost/'+id+'/url',)
    return postLink

# delete first line


def delete(id):
    return dataBaseColab.delete(databaseUrlColab, 'data/topost/'+id+'/url')

# last post link
def posted(title,posted_link):
    # print(title,posted_link)
    insertData('data/posted', {title:posted_link}, dataBaseColab,format='patch')



def initialDatabase(databaseUrl):
    dataBase = firebase.FirebaseApplication(
        databaseUrl, None)
    return dataBase


def updateToFirebase(title, category, data, dataBase):
    dataNew = {}
    dataNew[title.replace(".","-")] = data
    # dataNew={
    #     "bikeName":{
    #         "table1":{
    #             "key1":"value1",
    #             "key2":"value2",
    #             "key3":"value3"
    #         },
    #         "table2":{
    #             "key4":"value4",
    #             "key5":"value5",
    #             "key6":"value6"
    #         }
    #     }
    # }
    # print(dataNew)
    try:
        # print(category, dataNew, dataBase)
        insertData(category, dataNew, dataBase, format="patch")
        return 'uploaded'
    except Exception as e:
        print(e)
        return "failed"
    pass


def Run():
    toPostList = initialize()
    # print(toPostList)
    # return
    count=0
    # try:file=open("./data/posted.txt","a")
    # except:
    #     open("./data/posted.txt","w").close()
    #     file=open("./data/posted.txt","a")
    # try:file1=open("./data/postedlink.txt","a")
    # except:
    #     open("./data/postedlink.txt","w").close()
    #     file1=open("./data/postedlink.txt","a")
    

    for i in range(noOfPost):

        url = read(toPostList[i])
        #print(url)
        if(url==""):
            urlexract.run()
            url = read(toPostList[i])
            if(url==""):
                print("No new posts")
                break
        # print(url)
        try:
            title, category, tableDatas = ScrapTable.getdata(url)
        except Exception as e:
            print(e)
            break
        if(i<9):
            print(" ",end="")
        dataBase = initialDatabase(databaseUrl)
        print(i+1,end=">>>")
        print(title.split(" |")[0],end="")
        print("-"*(45-len(title.split(" |")[0])),end="status:")
        # import json
        # open("test.json", 'w').write(json.dumps(tableDatas))
        status=updateToFirebase(title, category, tableDatas, dataBase)

        print(status)
        if(status=="failed"):
            break
        
        title = title.replace(".", "-")
        posted(title,url)
        # file1.write(url+"\n")
        insertData('data/postedLinksInFirebase',{title: url}, dataBaseColab, format='patch')

        # file.write(title.split(" |")[0]+"\n")
        insertData('data/postedTitleInFireabase', {title:"title"}, dataBaseColab,format='patch')
        # print(toPostList[i])
        # print(toPostList[i])
        delete(toPostList[i])
        count=i+1

    print(count," post uploaded")




if __name__=="__main__":
    Run()
    # posted("a","b")
    pass
