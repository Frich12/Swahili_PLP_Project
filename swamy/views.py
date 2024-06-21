from django.shortcuts import render, get_object_or_404

from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

from django.shortcuts import render, get_object_or_404
from.models import Module

def module_detail (request, module_id):
    module = get_object_or_404(Module, id=module_id)
    return render(request, 'module_detail.html',{'module': module})

from django.shortcuts import render, get_object_or_404
from.models import Course, Module , Lesson

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})