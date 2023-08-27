from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin, BaseUserManager
# Create your models here.
from django import forms

class CustomUserManager(BaseUserManager):
 
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number must be set')
      
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, phone_number, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')

    #     return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(CustomUser, related_name="course_students", blank=True)
    teacher = models.ForeignKey(CustomUser, related_name="course_teacher", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.CharField(max_length=200)
    course = models.ForeignKey(Course, related_name="course_lesson", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

