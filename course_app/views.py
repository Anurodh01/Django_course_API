from django.shortcuts import render
from .models import Course, Instructor
from .serializers import CourseSerializer, InstructorSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
# Create your views here.
from rest_framework import generics


#to get the custom permission for the write by on admin
class writebyadminonly(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        user= request.user
        # x= authenticate(user= user)
        if request.method=="GET":
            return True
        if request.method=="POST" or request.method=='PUT' or request.method=="DELETE":
            if user.is_superuser:
                return True
        return False


class CourseListCreateView(generics.ListCreateAPIView):
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated,writebyadminonly]
    queryset= Course.objects.all()
    serializer_class= CourseSerializer

class CourseRetrieveUpdateDestriyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[BasicAuthentication]
    permission_classes= [IsAuthenticated, writebyadminonly]
    queryset = Course.objects.all()
    serializer_class= CourseSerializer

class InstructorListCreateView(generics.ListCreateAPIView):
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]
    queryset= Instructor.objects.all()
    serializer_class= InstructorSerializer

class InstructorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticated]
    queryset= Instructor.objects.all()
    serializer_class= InstructorSerializer
