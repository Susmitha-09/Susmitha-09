from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')
def profile_picture(request):
    return render(request,'myapp/profile_picture.html')
def education(request):
    return render(request,'myapp/education.html')
def technical_skills(request):
    return render(request,'myapp/technical_skills.html')
def research(request):
    return render(request,'myapp/research.html')
def strengths(request):
    return render(request,'myapp/strengths.html')
def certifications_workshops(request):
    return render(request,'myapp/certifications_workshops.html')
def project_experience(request):
    return render(request,'myapp/project_experience.html')
def achievements(request):
    return render(request,'myapp/achievements.html')
def extracurricular_activities(request):
    return render(request,'myapp/extracurricular_activities.html')
def hobbies(request):
    return render(request,'myapp/hobbies.html')
def personal_details(request):
    return render(request,'myapp/personal_details.html')
