from __future__ import print_function

import sys
import time
from oauth2client import client
from googleapiclient import sample_tools




def main(argv):
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
            "id": "6814573853229626501",
            "title": "posted via python",
            "content": "<div>hello world test</div>"
        }
        blog = thisusersblogs['items'][0]
        if blog['id'] == '7109014683179605133':
            posts.insert(blogId=blog['id'],
                         body=body, isDraft=True).execute()

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize')


if __name__ == '__main__':
    for i in range(150):
        print(i)
        main(sys.argv)
        time.sleep(10)
