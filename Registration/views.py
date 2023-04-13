from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from Registration.utils import get_db_handle, get_collection_handle


DATABASE_NAME = 'hr-portal'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '27017'
db_handle, mongo_client = get_db_handle(DATABASE_NAME, DATABASE_HOST, DATABASE_PORT)
collection = db_handle['login']

# Create your views here.
def home(request):
    return render(request,'register.html')

    
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    dic = {}
    cursor = collection.find({},{"email": 1,"password":1})
    for i in cursor:
        dic[i['email']] = i['password']
    if email in dic.keys() and password in dic.values():
        return render(request,'profile.html')
    elif email in dic.keys() and password not in dic.values():
        return render(request,'register.html',{'message': 'Incorrect Password'})
    else:
        return render(request,'register.html',{'message': 'Incorrect Email and Password'})
    

    

