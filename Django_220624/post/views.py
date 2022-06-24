from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q
from post.serializers import JobPostSerializer



class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)
        job_serializer = JobPostSerializer(data=request.data)
        
        if job_serializer.is_valid():
            job_serializer.save()
            return Response(job_serializer.data, status=status.HTTP_200_OK)
        
        print('29 : ',job_type, company_name)
        
        print('31 : ',request)
        return Response(job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

