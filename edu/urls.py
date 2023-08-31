from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'get_index'),
    path('sign-up/', views.sign_up, name = 'sign_up'),
    path('sign-in/', views.sign_in, name = 'sign_in'),
    path('my_profile/', views.get_profile, name = 'get_profile'),
    path('courses/', views.get_courses, name = 'get_courses'),
    path('courses/<int:course_id>/', views.course_detail, name = 'course_detail'),
    path('teacher/', views.teacher, name = 'teacher'),
    path('chat/', views.chat, name='chat'),
    path('chat/ask/<str:question>', views.ask_gpt3, name='ask_gpt3'),
]   
