from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .models import Course, Lesson, CustomUser
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomUserLoginForm, CourseForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, 'edu/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'edu.backends.PhoneNumberBackend'
            group = Group.objects.get(name = "student")
            group.user_set.add(user)
            login(request, user)
            return HttpResponseRedirect(reverse('get_index'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/sign-up.html', {'form': form})

    
    
def sign_in(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['username'] = post_data.get('phone_number')  # Copy phone_number to username
        form = CustomUserLoginForm(request, data=post_data)
        if form.is_valid():
            phone_number = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                user.backend = 'edu.backends.PhoneNumberBackend'
                login(request, user)
                return HttpResponseRedirect(reverse('get_index'))
            else:
                form.add_error("Қате телефон номері немесе құпиясөз")
        else:
            print("Form is not valid")
    else:
        form = CustomUserLoginForm()
    
    return render(request, 'registration/sign-in.html', {'form': form})

def get_profile(request):
    group_name = None
    for group in request.user.groups.all():
        group_name = group.name
    
    return render(request, 'edu/profile.html', {'group_name': group_name})

def get_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'edu/courses.html', {'courses': courses})
def get_chat(request):
    pass

def course_detail(request, course_id):
    course = get_object_or_404(Course.objects.prefetch_related('course_lesson'), id=course_id)
    user = request.user
    is_enrolled = course.students.filter(id=user.id).exists()
    if request.method == 'POST':
        course.students.add(user)
        return HttpResponseRedirect(reverse('course_detail', args=[course_id]))
    
    for lesson in course.course_lesson.all():
        lesson.video_url = "https://www.youtube.com/embed/" + lesson.video_url[-11:]
    return render(request, 'edu/course_detail.html', {'course' : course, 'is_enrolled': is_enrolled})
    

@login_required    
def teacher(request):
    teacher = request.user
    courses_of_teacher = Course.objects.filter(teacher=teacher).order_by('-created_at')
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = teacher 
            course.save()  
            return HttpResponseRedirect(reverse('get_courses'))
    return render(request, 'edu/teacher.html', {'form' : form, 'courses' : courses_of_teacher})
    

        


   

    
