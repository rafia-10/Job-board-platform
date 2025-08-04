from rest_framework import serializers
from .models import Job, Category, Application

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Job
        fields = '__all__'
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category= Category.objects.create(**category_data)
        job = Job.objects.create(category=category, **validated_data)
        return job


# class ApplicationSerializer(serializers.ModelSerializer):
#     job = JobSerializer(read_only=True)
#     user = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = Application
#         fields = '__all__'
#         read_only_fields = ('applied_at',)