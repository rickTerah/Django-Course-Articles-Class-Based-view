from django.urls import path
# from .views import course_list_view
from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseDeleteView,
    CourseUpdateView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name = "course_list"),
    path('<int:id>/', CourseDetailView.as_view(), name = "course_detail"),
    path('create/', CourseCreateView.as_view(), name = "course_create"),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name = "course_delete"),
    path('<int:id>/update/', CourseUpdateView.as_view(), name = "course_update")
]