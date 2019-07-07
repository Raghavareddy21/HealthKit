from django import forms
from .models import *
class PatientSignup(forms.ModelForm):
	class Meta:
		model = UserDetails
		fields=('username','password','name','age','aadharNumber','email','languages','phoneNumber')
class OtherDetail(forms.ModelForm):
	class Meta:
		model = OtherDetails
		fields=('user','specialization','degree')
class PatientRequest(forms.ModelForm):
	class Meta:
		model = PatientRequest
		fields=('patient','doctor','Symtomps','date')
class DoctorResponse(forms.ModelForm):
	class Meta:
		model = DoctorResponse
		fields=('doctor','patient','request','Solution','date')
class MedicalCamp(forms.ModelForm):
	class Meta:
		model = MedicalCamp
		fields = ('Creator','numberOfPeopleIll','address','date')