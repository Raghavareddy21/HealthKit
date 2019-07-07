from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
	url(r'^signup/$',views.patientSignup,name="signup"),
	url(r'^Home/$',views.Home,name="Home"),
	url(r'^login/$',views.Doctorlogin,name="login"),
	url(r'^patientRequest/$',views.patientRequest,name="patientRequest"),
	url(r'^doctorSolution/$',views.doctorSolution,name="doctorSolution"),
	url(r'^doctorSolutions/$',views.doctorSolutions,name="doctorSolutions"),
	url(r'^patientRequests/$',views.patientRequests,name="patientRequests"),

]