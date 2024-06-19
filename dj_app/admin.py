from django.contrib import admin
from .models import  PersonalDetail, Experience, Education, Project

# Register your models here.

admin.site.register(PersonalDetail)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)

