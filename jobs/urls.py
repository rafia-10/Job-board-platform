from django.urls import path
from .views import JobListCreateAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    
]

