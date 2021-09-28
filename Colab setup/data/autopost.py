from __future__ import print_function
import sys
import sys
from oauth2client import client
from googleapiclient import sample_tools
import time
import re
# from sys import ps1
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup, dammit
from firebase import firebase
import pyrebase
from requests.models import ReadTimeoutError
from firebase import firebase

noOfPost = 100

databaseUrl = "https://colabfacebook-default-rtdb.firebaseio.com/Website/AllBikeSpecification/"
dataBase = firebase.FirebaseApplication(databaseUrl, None)

# def filemake(name):
#     try:
#         file=open(name,"r+")
#     except:
#         open(name,"w").close()
#         file=open(name,"r+")
#     return file


def initialize():
    dataSet = dataBase.get(databaseUrl, 'data/posted',)
    toPostList = list(dataSet.keys())[:noOfPost]
    return toPostList

def insertData(tableName, data, dataBase, format="post"):
    if(format == "patch"):
        result = dataBase.patch(tableName, data)
    else:
        result = dataBase.post(tableName, data)


# delete first line
def delete(bikeName):
    return dataBase.delete(databaseUrl, 'data/posted/'+bikeName)

# last post link


def posted(title):
    insertData('data/postedInBlogger',{title: "title"}, dataBase, format='patch')


def postTitlesInBlogger(postName, argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')
    return service
    try:
        users = service.users()

        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()

        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()

        posts = service.posts()
        body = {
            "kind": "blogger#post",
            "title": postName,
            "labels": [postName.split()[0]]
        }
        blog = thisusersblogs['items'][0]
        
        posts.insert(blogId="5317390335310223575",body=body, isDraft=True).execute()
        
        return "posted"

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run''the application to re-authorize')
        return "failed"


def Run():
    count = 0
    toPostList=initialize()

    for i in range(noOfPost):
        # time.sleep(10)
        postTitle = toPostList[i]
        #print(postTitle)
        if(postTitle == ""):
            print("No new posts")
            break
                

        if(i < 9):
            print(" ", end="")

        print(i+1, end=">>>")
        print(postTitle, end="")
        print("-"*(45-len(postTitle)), end="status:")
        #postnow(driver,ptitle,ptag,pdescri,pcontent,pimage):

        status = postTitlesInBlogger(postTitle, sys.argv)
        
        print(status)

        # postToblogger.postnow()
        if(status == "failed"):
            print("Exit!")
            break
        print("")

        posted(postTitle)
        delete()
        count = i+1
        time.sleep(10)


    print(count, " post posted")


print(postTitlesInBlogger("postName", sys.argv))
