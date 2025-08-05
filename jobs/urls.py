from django.urls import path
from .views import (JobListCreateAPIView, JobRetrieveUpdateDestroyAPIView, 
                    ApplicationListCreateAPIView, ApplicationRetrieveUpdateDestroyAPIView,ApplicationsListAPIView)

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobRetrieveUpdateDestroyAPIView.as_view(), name='job-detail'),
    path('applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationRetrieveUpdateDestroyAPIView.as_view(), name='application-detail'),
    path('jobs/<int:job_id>/applications/', ApplicationsListAPIView.as_view(), name='job-applications-list'),
]


