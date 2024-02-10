from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),
    path('index/', views.index, name='index'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_id>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('anime/', views.anime_view, name="anime_view"),
]