from django import forms
from django import forms
from .models import PersonalDetail, Experience, Education, Project


class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = ['name', 'email', 'phone', 'address']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['personal_detail', 'institution_name', 'degree', 'field_of_study']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['personal_detail', 'title', 'description', 'link']
