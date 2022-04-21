from django.shortcuts import render
from django.http import HttpResponse
from .models import user

from pymongo import MongoClient
# Create your views here.

client = MongoClient('localhost',27017)
rakdb = client["rakesh"]
rakcoll = rakdb["author"]
doc = rakcoll.find({"name" : "rakesh"})
signup_coll = rakdb["signup"]
data = doc.next()
print(data["name"])

#data = {"name":"sanjana"}
#rakcoll.insert_one(data)

#for i in rakcoll.find():
    #print(i)


def signup(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    signup_coll = rakdb["signup"]
    data = {"username":username,"password":password}
    check = signup_coll.count_documents({"username":username})
    print("data is :"+str(check))
    if(check):
        return render(request,'signup.html',{"msg":"username already exits"})
    else:
        signup_coll.insert_one(data)
        return render(request,'signup.html',{"msg":"signup completed"})


def login(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    if(signup_coll.count_documents({"username":username,"password":password}) and username != None ):
        request.session['username'] = username
        return render(request,'chatpage.html',{"username": username})
    else:
        return render(request,'login.html',{"msg":"username or password is wrong"})

def index(request):
    user1 = user()
    user1.name = "rakesh"
    user1.status = "online"

    user2 = user()
    user2.name = data["name"]
    user2.status = "offline"

    users = [user1, user2,]

    chat_history1 = ["hi baby","i love you",]
    chat_history2 = ["hi","love you too",]
    return render(request,'index.html',{'users':users,'chathistory1':chat_history1,'chathistory2':chat_history2})





def chat_page(request):
    username = request.session["username"]
    print("data is:")
    print(username)
    user1 = user()
    user1.name = "rakesh"
    user1.status = "online"

    user2 = user()
    user2.name = data["name"]
    user2.status = "offline"

    users = [user1, user2,]

    chat_history1 = ["hi ","i love you baby",]
    chat_history2 = ["hi","love you too baby",]
    return render(request,'chatpage.html',{'users':users,'chathistory1':chat_history1,'chathistory2':chat_history2})