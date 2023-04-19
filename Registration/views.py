from django.shortcuts import render,redirect
from Registration.models import emp_details,announcements,Attendance
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
    attendance_data = Attendance.objects.all()
    attendance_data = Attendance.objects.filter(user=request.session['username'])
  
    return render(request,'att.html',context = {'attendance_data': attendance_data}) 

def request(request):
    return render(request,'request.html') 
   
def checkinn(request):
    if request.method == 'POST':
        attendance = Attendance(user=request.session['username'])
        attendance.save()
        attendance.check_date()
    return render(request, 'checkin.html')

def checkin(request):
    attendance_data = Attendance.objects.all()
    attendance_data = Attendance.objects.filter(user=request.session['username'])
  
    return render(request,'attendance_data.html',  context = {'attendance_data': attendance_data})
    #return HttpResponse("Hello, world. You're at the polls index.")

def checkout(request):
    attendance = Attendance.objects.filter(user=request.session['username'], check_out__isnull=True).first()
    if attendance:
        attendance.save()
        attendance.check_out_user()    
    else:
        # Attendance record not found for today
        check_in_time = None
        check_out_time = None
        hours_worked = None
        present = False    
    return redirect('checkin')

def logout(request):
    return redirect('/login')