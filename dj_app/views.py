from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetail, Experience, Education, Project
from .form import PersonalDetailForm, ExperienceForm, EducationForm, ProjectForm


def person(request):
    personal_details = PersonalDetail.objects.all()
    experi = Experience.objects.all()
    Edu = Education.objects.all()
    proj = Project.objects.all()

    return render(request, 'base.html',
                  {'personal_details': personal_details, 'experi': experi, 'Edu': Edu, 'proj': proj})
