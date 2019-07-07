from django.shortcuts import render, redirect
from .forms import *
from . models import *
from django.http import HttpResponse
from . forms import PatientRequest
from  .models import PatientRequest as preq
from . models import UserDetails as UserDetails
from . models import MedicalCamp as MedicalCamp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
def patientSignup(request):
	if request.method == 'POST':
		form = PatientSignup(request.POST)
		if form.is_valid():
			form.instance.is_patient=True
			form.save()
			return redirect('/HealthKit/Home/')
		else:
			return render(request, 'HealthKit/signup.html', {'form': form})
	else:
		form = PatientSignup()
	return render(request, 'HealthKit/signup.html', {'form': form})
def Home(request):
	return render(request,'HealthKit/Home.html')
def Doctorlogin(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in")
    else:
        if request.method == 'POST':
            usernames = request.POST.get('username')
            passwords = request.POST.get('password')
            user = authenticate(username=usernames,
             password=passwords)
            if user is not None:
                auth_login(request, user)
                return redirect('/HealthKit/Home/')
            else:
            	return HttpResponse('Wrong credentials provided')
                # return render(request, 'HealthKit/login.html', {'err': 'Wrong credentials provided'})
        else:
            return render(request, 'HealthKit/login.html', {'err': ''})
def patientRequest(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form=PatientRequest(request.POST)
			if form.is_valid():
				form.save()
				return render(request,'HealthKit/patientRequests.html')
			else:
				return render(request,'HealthKit/patientRequest.html')
		else:
			form=PatientRequest()
			return render(request,'HealthKit/patientRequest.html',{'form':form})
	else:
		return HttpResponse("You need to login as patient to add request")
def doctorSolution(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form=forms.DoctorResponse(request.POST)
			if form.is_valid():
				form.save()
				return request(request,'HealthKit/doctorSolutions.html')
			else:
				return render(request,'HealthKit/doctorSolution.html')
		else:
			form=forms.DoctorResponse()
			return render(request,'HealthKit/doctorSolution.html',{'form':form})
	else:
		return HttpResponse("You need to login as doctor to add request")

def doctorSolutions(request):
	if request.user.is_authenticated:
		doctorsDetails=UserDetails.objects.all()
		doctors=doctorsDetails.objecfts.filter(doctorsDetails.is_doctor==True)
		DoctorResponses=DoctorResponse.objects.filter(doctors.username==amma)
		return render(request,'HealthKit/doctorSolutions.html',{'DoctorResponses':DoctorResponses})
	else:
		return HttpResponse("You need to login as doctor to add request")
def patientRequests(request):
	if request.user.is_authenticated:
		PatientRequests=preq.objects.all()
		return(request,'HealthKit/patientRequests.html',{'PatientRequests':PatientRequests})
	else:
		return HttpResponse("You need to login as patient to add request")
def doctorList(request,pk):
	if request.user.is_authenticated:
		doctor=models.UserDetails.objects.get(pk=pk)
		return render(request, 'HealthKit/doctorList.html',{'doctor':doctor})
	else:
		return HttpResponse("you need to login to access doctorList")
def MedicalCamp(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form=forms.MedicalCamp(request.POST)
			if form.is_valid():
				form.save()
				return render(request,'HealthKit/MedicalCamps.html')
			else:
				return render(request,'HealthKit/MedicalCamp.html')
		else:
			form=PatientRequest()
			return render(request,'HealthKit/MedicalCamp.html',{'form':form})
	else:
		return HttpResponse("You need to login as patient to add request")
def MedicalCamps(request):
	if request.user.is_authenticated:
		MedicalCamps=MedicalCamp.objects.all()
		return render(request, 'HealthKit/MedicalCamps.html',{'MedicalCamps':MedicalCamps})
	else:
		return HttpResponse("you need to login to access MedicalCamps")
def DoctorsList(request):
	if request.user.is_authenticated:
		Doctors=UserDetails.objects.all()
		Doc=UserDetails.objects.filter(UserDetails.is_doctor==True)
		return render(request,'HealthKit/doctorsList.html',{'Doc':Doctors})
	else:
		return HttpResponse("you need to login to access DoctorsList")
def Knowledge(request):
	return render(request,'HealthKit/Knowledge.html')