from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
# Create your models here.
class Language(models.Model):
	name=models.CharField(max_length=20,verbose_name="Language Name", primary_key=True)
	def __str__(self):
		return self.name
class UserDetails(models.Model):
	name=models.CharField(max_length=50, verbose_name="Name")
	username=models.CharField(max_length=25,verbose_name="username")
	password=models.CharField(max_length=15,verbose_name="password")
	age=models.IntegerField(validators=[MaxValueValidator(100)],verbose_name="Age")
	aadharNumber=models.IntegerField(validators=[MaxValueValidator(999999999999)],verbose_name="Aadhar Number")
	email=models.EmailField(blank=False, max_length=60, verbose_name="Email Address")
	languages=models.ManyToManyField(Language)
	is_doctor=models.BooleanField(default=False)
	is_patient=models.BooleanField(default=False)
	phoneNumber=models.IntegerField(validators=[MaxValueValidator(9999999999)],verbose_name="Phone Number")
	def __str__(self):
		return self.username
class OtherDetails(models.Model):
	user = models.OneToOneField(UserDetails, on_delete=models.CASCADE, primary_key=True)
	specialization=models.CharField(max_length=50,verbose_name="Specialization")
	degree=models.TextField()
	def __str__(self):
		return self.user.username
class PatientRequest(models.Model):
	patient=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='patient1')
	doctor=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='doctor1')
	Symtomps=models.CharField(max_length=300,verbose_name="Symtomps")
	date=models.DateField()
	def __int__(self):
		return self.id
class DoctorResponse(models.Model):
	doctor=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='doctor2')
	patient=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='patient2')
	request=models.ForeignKey(PatientRequest,on_delete=models.CASCADE)
	Solution=models.CharField(max_length=300,verbose_name="Solutions")
	date=models.DateField()
	def __int_(self):
		return self.id