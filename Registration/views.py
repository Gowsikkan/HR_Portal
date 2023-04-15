from django.shortcuts import render,redirect
from Registration.models import emp_details,announcements
from django.contrib import messages
# Create your views here.

def login(request):
    
    if request.method =="POST":
        id= request.POST['emp_id']
        password = request.POST['password']
        request.session['username'] = id
        if emp_details.objects.filter(emp_id=id, password=password).exists():
            return redirect('/home')
        else:
            return render(request,'login.html',{'message': 'Incorrect Password'})
    else:
        return render(request,'login.html')
    
def home(request):
    return render(request,'home.html') 

def directory(request):
    
    if request.session.has_key('username'):
        cursor = emp_details.objects.all()
        print(cursor)
        return render(request,'directory.html',{'cursor':cursor}) 
    else:
        return redirect('/login')
def annoucement(request):
    details = announcements.objects.all()
    return render(request,'announcement.html',{'details':details}) 

def attendence(request):
    return render(request,'attendence.html') 

def request(request):
    return render(request,'request.html') 

def checkin(request):
    return render(request,'checkin.html') 

def logout(request):
    return redirect('/login')