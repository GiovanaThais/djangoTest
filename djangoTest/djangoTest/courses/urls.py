from django.urls import path
from .views import CourseList,CourseCreate,CourseUpdate,CourseDelete


urlpatterns = [
    path('',CourseList.as_view(),name='cursos_list'),
    path('create/',CourseCreate.as_view(),name='cursos_create')
    path('update/<pk::int>/',CourseUpdate.as_view(),name='cursos_update')
    path('delete/<pk::int>/',CourseDelete.as_view(),name='cursos_delete')
] 