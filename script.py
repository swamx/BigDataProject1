#Please dont use the script for a single page of commit 
import requests
import json
import pymongo
import urllib
import pprint

# Database connection string 
from pymongo import MongoClient
ip = "localhost"
port = "37001"
conn_str = ""
client = MongoClient(conn_str)
db = client.hadoop
col =db.commit
def get_commit_url(link):
    for l in link.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return str(a.strip()[1:-1])
url = 'https://api.github.com/repos/apache/hadoop/commits'
req = requests.get(url)
commit_data = json.loads(req.content)
link=get_commit_url(req.headers.get('link'))
for commit in commit_data:
    try:
        col.insert_one(commit)
    except:
        print("Duplicate Object May be present")

while link is not None:
    req = requests.get(link)
    commits_data=json.loads(req.content)
    for commit in commit_data:
        try:
            col.insert_one(commit)
        except:
            print(type(commit))
            print(commit)
            print("Duplicate Object May be present")
            break
    if not (req.headers.get('link')):
        link = None
        print("Scan completed")
    else:
        link = get_commit_url(req.headers.get('link'))        
