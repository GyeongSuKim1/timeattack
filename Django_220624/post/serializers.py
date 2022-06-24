from rest_framework import serializers
from post.models import JobPost as JobPostModel



class JobPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPostModel
        fields = "__all__"