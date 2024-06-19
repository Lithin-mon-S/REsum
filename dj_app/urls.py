from django.urls import path
from . import views

urlpatterns = [
    path('', views.person, name='personal_detail_list'),
   # path('personal_details/new/', views.personal_detail_create, name='personal_detail_create'),
    #path('personal_details/<int:pk>/edit/', views.personal_detail_update, name='personal_detail_update'),
    #path('personal_details/<int:pk>/delete/', views.personal_detail_delete, name='personal_detail_delete'),

    #path('experiences/', views.experience_list, name='experience_list'),
    #path('experiences/new/', views.experience_create, name='experience_create'),
    #path('experiences/<int:pk>/edit/', views.experience_update, name='experience_update'),
    #path('experiences/<int:pk>/delete/', views.experience_delete, name='experience_delete'),

    #path('educations/', views.education_list, name='education_list'),
    #path('educations/new/', views.education_create, name='education_create'),
    #path('educations/<int:pk>/edit/', views.education_update, name='education_update'),
    #path('educations/<int:pk>/delete/', views.education_delete, name='education_delete'),

    #path('projects/', views.project_list, name='project_list'),
    #path('projects/new/', views.project_create, name='project_create'),
    #path('projects/<int:pk>/edit/', views.project_update, name='project_update'),
    #path('projects/<int:pk>/delete/',views.project_delete,name='project_delete')


]
