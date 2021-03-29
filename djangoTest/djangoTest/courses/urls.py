from django.urls import path
from .views import CourseList,CourseCreate,CourseUpdate,CourseDelete


urlpatterns = [
    path('',CourseList,name='cursos_list'),
    path('create/',CourseCreate,name='cursos_create')
    path('update/<pk::int>/',CourseUpdate,name='cursos_update')
    path('delete/<pk::int>/',CourseDelete,name='cursos_delete')
] 