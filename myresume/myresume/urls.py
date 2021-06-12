"""myresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views
from myapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    # url(r'^myapp/',include('myapp.urls')),
    url(r'^about/',views.about,name='about'),
    url(r'^profile_picture/',views.profile_picture,name='profile_picture'),
    url(r'^education/',views.education,name='education'),
    url(r'^technical_skills/',views.technical_skills,name='technical_skills'),
    url(r'^research/',views.research,name='research'),
    url(r'^strengths/',views.strengths,name='strengths'),
    url(r'^certifications_workshops/',views.certifications_workshops,name='certifications_workshops'),
    url(r'^project_experience/',views.project_experience,name='project_experience'),
    url(r'^achievements/',views.achievements,name='achievements'),
    url(r'^extracurricular_activities/',views.extracurricular_activities,name='extracurricular_activities'),
    url(r'^hobbies/',views.hobbies,name='hobbies'),
    url(r'^personal_details/',views.personal_details,name='personal_details'),

]
