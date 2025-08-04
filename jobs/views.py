from django.shortcuts import render

import django_filters
from rest_framework import permissions, generics, filters
from .models import Job, Application, Category
from .serializers import JobSerializer,  CategorySerializer


class JobListCreateAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'location', 'job_type', 'company']
    permission_classes = [permissions.AllowAny]