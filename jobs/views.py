from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework import permissions,  filters
from .models import Job, Application, Category
from .serializers import JobSerializer,  CategorySerializer, ApplicationSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class JobListCreateAPIView(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'location', 'job_type', 'company']
    permission_classes = [permissions.AllowAny]


class JobRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

# class JobApplicationCreateAPIView(CreateAPIView):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         job_id = self.kwargs.get('job_id')
#         job = Job.objects.get(id=job_id)
#         serializer.save(job=job)

# create and list applications
class ApplicationListCreateAPIView(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job', 'full_name','email']
    permission_classes = [permissions.AllowAny]


# Delete, update, retrieve a single application
class ApplicationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]

#List application by job id
class ApplicationsListAPIView(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Application.objects.filter(job_id=job_id)

