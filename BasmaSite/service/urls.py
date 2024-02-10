from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('serverc/', views.service_list, name='service_list'),
    path('service/add/', views.service_create, name='service_create'),
    path('service/update/<int:service_id>/', views.service_update, name='service_update'),
    path('service/delete/<int:service_id>/', views.service_delete, name='service_delete'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('service/<int:service_id>/request/', views.service_request, name='service_request'),
    path('request/<int:request_id>', views.update_service_request, name='update_service_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('manager/requests/', views.manager_requests, name='manager_requests'),
]