from django.contrib import admin
from .models import Course, Lesson, CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number']
    
admin.site.register(CustomUser, CustomUserAdmin)

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 5

class NewsAdmin(admin.ModelAdmin):  # Возможно, это должно быть CourseAdmin?
    list_display = ('title', 'description')  # Исправлено 'descrtiption' на 'description'
    inlines = [LessonInline]

admin.site.register(Course, NewsAdmin)  # Регистрация с использованием NewsAdmin

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 

admin.site.register(Lesson, LessonAdmin) 