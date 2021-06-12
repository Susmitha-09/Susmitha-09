from django.conf.urls import url
from myapp import views

# app_name = 'myapp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about$',views.about,name='about'),
    url(r'^profile_picture$',views.profile_picture,name='profile_picture'),
    url(r'^education$',views.education,name='education'),
    url(r'^technical_skills$',views.technical_skills,name='technical_skills'),
    url(r'^research$',views.research,name='research'),
    url(r'^strengths$',views.strengths,name='strengths'),
    url(r'^certifications_workshops$',views.certifications_workshops,name='certifications_workshops'),
    url(r'^project_experience$',views.project_experience,name='project_experience'),
    url(r'^achievements$',views.achievements,name='achievements'),
    url(r'^extracurricular_activities$',views.extracurricular_activities,name='extracurricular_activities'),
    url(r'^hobbies$',views.hobbies,name='hobbies'),
    url(r'^personal_details$',views.personal_details,name='personal_details'),
]
