# from rest_framework import serializers
# from .models import Job, Category, Application

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
    

# class JobSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = Job
#         fields = '__all__'

# class ApplicationSerializer(serializers.ModelSerializer):
#     job = JobSerializer(read_only=True)
#     user = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = Application
#         fields = '__all__'
#         read_only_fields = ('applied_at',)