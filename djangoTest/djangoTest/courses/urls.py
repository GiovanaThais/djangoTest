from django.urls import path
from .views import CourseList,CourseCreate,CourseUpdate,CourseDelete


urlpatterns = [
    path('',CourseList.as_view(),name='course_list'),
    path('create/',CourseCreate.as_view(),name='course_create')
    path('update/<pk::int>/',CourseUpdate.as_view(),name='course_update')
    path('delete/<pk::int>/',CourseDelete.as_view(),name='course_delete')
] 