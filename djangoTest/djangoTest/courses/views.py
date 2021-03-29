from django.shortcuts import render
from django.views.generic import ListView,CreateView, UpdateView,DeleteView 
from .models import Course
from django.http import HttpResponse

class CourseList(ListView):
    model = Course

class CourseCreate(CreateView):
    model = Course

class CourseUpdate(UpdateView):
    model = Course

class CourseDelete(DeleteView):
    model = Course