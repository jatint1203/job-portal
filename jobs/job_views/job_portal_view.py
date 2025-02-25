# API Views
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import Job, Application
from jobs.serializers import JobSerializer, ApplicationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

class JobListView(APIView):

    def get(self, request):
        jobs = Job.objects.filter(delete_flag=False)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            request.data['posted_by'] = request.user.id
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()


class ApplicationListView(APIView):

    def get(self, request):
        applications = Application.objects.filter(delete_flag=False, applicant=request.user.id)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['applicant'] = request.user.id
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save(=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

