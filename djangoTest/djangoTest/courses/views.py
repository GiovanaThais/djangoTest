from django.shortcuts import render
from django.views.generic import ListView,CreateView, UpdateView,DeleteView 
from .models import Course
from django.urls import reverse_lazy
from django.http import HttpResponse

class CourseList(ListView):
    model = Course
    

class CourseCreate(CreateView):
    model = Course
    fields = ['nome','data','descricao']
    success_url = reverse_lazy('cliente_list')

class CourseUpdate(UpdateView):
    model = Course
    fields = ['nome','data','descricao']
    success_url = reverse_lazy('cliente_list')
class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('cliente_list')