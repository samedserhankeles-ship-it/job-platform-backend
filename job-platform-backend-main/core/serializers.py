from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        
        fields = [
            'id', 
            'user', 
            'title', 
            'description', 
            'location_city',
            'created_at'
        ]
        
        read_only_fields = [
            'id', 
            'user', 
            'created_at' 
        ]
