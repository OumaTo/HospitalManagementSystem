from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import *
from django.contrib.auth.forms import AuthenticationForm
from HMS.models import *
from django.contrib import messages 


# Create your views here.
def index(request):
    data = Statistic.objects.all().values()
    context ={
        'data':data
    }
    return render(request, 'HMS/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
           
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print('welcome')
                login(request, user)

                return redirect('staff')
        else:
            print('not recognizeed')

    form = AuthenticationForm()

    return render(request, 'HMS/login.html',{'form':form,})


# @login_required
def staff(request):
    data = Statistic.objects.all().values()
    patients = Patient.objects.all().values()
    appointment = Appointment.objects.all().values()
    context ={
        'data':data,
        'patients':patients,
        'appointments':appointment
    }
    return render(request, 'HMS/analysis.html', context)

def appointments(request):
    if request.method =='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        category = request.POST.get('category')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        date = request.POST.get('date')
        situation = request.POST.get('situation')

        new_appointment = Appointment(FirstName = firstname, LastName =lastname, Age= age, Phone=phone, Category = category, Date = date, Description = description, Situation = situation )
        new_appointment.save()

        messages.add_message(request, messages.INFO, "Booking Successfull")
    
    return render(request, 'HMS/appointments.html')
