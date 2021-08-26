import os
import sys
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


noOfPost=200


accNO=0
if(len(sys.argv)>1):
    accNO=int(sys.argv[1])
# read first line
def read():
    file = open("./data/topost.txt", "r", encoding='utf-8')
    firLi=file.readline().replace("\n","")
    file.close()
    return firLi

# delete first line
def delete():
    file=open("./data/topost.txt","r")
    firLi=file.readlines()
    file.close()
    file=open("./data/topost.txt","w")
    file.write("".join(firLi[1:]))
    file.close()

# last post link
def posted(posted_link):
    file=open("./data/lastpost.txt","w")
    file.write(posted_link)
    file.close()


def insertData(tableName, data, dataBase, format="post"):
    if(format == "patch"):
        result = dataBase.patch(tableName, data)
    else:
        result = dataBase.post(tableName, data)


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
    except:
        return "failed"
    pass


def Run():
    count=0
    try:file=open("./data/posted.txt","a")
    except:
        open("./data/posted.txt","w").close()
        file=open("./data/posted.txt","a")
    try:file1=open("./data/postedlink.txt","a")
    except:
        open("./data/postedlink.txt","w").close()
        file1=open("./data/postedlink.txt","a")
    

    for i in range(noOfPost):

        url=read()
        #print(url)
        if(url==""):
            urlexract.run()
            url=read()
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
        status=updateToFirebase(title, category, tableDatas, dataBase)

        print(status)
        if(status=="failed"):
            break

        posted(url)
        file1.write(url+"\n")
        file.write(title.split(" |")[0]+"\n")
        delete()
        count=i+1
    file1.close()
    file.close()

    print(count," post uploaded")




# Run()
data = {
    "bikeName": {
        "table1": {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        },
        "table2": {
            "key4": "value4",
            "key5": "value5",
            "key6": "value6"
        }
    }
}
title="Bmw new modle"
category="BMW"
# dataBase = initialDatabase(databaseUrl)

# status=updateToFirebase(title, category, data, dataBase)
# print(status)
Run()
