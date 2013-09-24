from __future__ import print_function
import urllib2, sys
import json
import codecs
import datetime

isEvent = False
if len(sys.argv) != 2:
    sys.exit("Invalid Arguments")
page = sys.argv[1]
now = datetime.datetime.now()
response = urllib2.urlopen('https://graph.facebook.com/'+str(page))
data = json.load(response,"utf-8")
if "venue" in data.keys():
    isEvent = True
    response = urllib2.urlopen('https://graph.facebook.com/'+page+'?fields=name,description,picture')
else:
    response = urllib2.urlopen('https://graph.facebook.com/'+page+'?fields=name,about,picture,description')
data = json.load(response,"utf-8")  
if "error" in data.keys():
    sys.exit("Invalid Facebook page")
filename="_posts/"+now.strftime("%Y-%m-%d-")+page+".markdown"
f=codecs.open(filename,'w', "utf-8")
if not "about" in data.keys():
    data["about"]=" "
if not "description" in data.keys():
    data["description"]=" "
print("---",file=f)
print("layout:  post",file=f)
print("title: "+ "\""+data["name"]+"\"",file=f)
print("date: "+ now.strftime('%Y-%m-%d %H:%M:%S') ,file=f)
print("name: "+ "\""+data["name"]+"\"",file=f)
if isEvent:
    print("faceurl: "+"\""+"http://facebook.com/events/"+page+"\"",file=f)
else:
    print("faceurl: "+"\""+"http://facebook.com/"+page+"\"",file=f)
print("about: "+ "\""+data["about"]+"\"",file=f)
print("description: "+ "\""+data["description"]+"\"",file=f)
print("faceurl: "+"\""+"http://facebook.com/"+page+"\"",file=f)
print("imgurl: "+ "\""+data["picture"]["data"]["url"]+"\"",file=f)
print("---",file=f)
