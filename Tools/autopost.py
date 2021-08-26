from __future__ import print_function
import sys
import sys
from oauth2client import client
from googleapiclient import sample_tools
import time

noOfPost = 99


def filemake(name):
    try:
        file=open(name,"r+")
    except:
        open(name,"w").close()
        file=open(name,"r+")
    return file


def read():
    file = open("./data/posted.txt", "r")
    firLi = file.readline().replace("\n", "")
    file.close()
    return firLi

# delete first line


def delete():
    file = open("./data/posted.txt", "r")
    firLi = file.readlines()
    file.close()
    file = open("./data/posted.txt", "w")
    file.write("".join(firLi[1:]))
    file.close()

# last post link


def posted(posted_link):
    file = open("./data/postTitleInBlogger.txt", "a")
    file.write(posted_link+"\n")
    file.close()


def postTitlesInBlogger(postName, argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')

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

    for i in range(noOfPost):
        # time.sleep(10)
        postTitle = read()
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


    print(count, " post posted")



Run()
input()