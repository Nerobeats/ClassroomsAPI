from django.shortcuts import render
from .serializers import RegisterSerializer , ClassroomDetailsSerializer , ClassroomSerializer ,UpdateClassroomSerializer,CreateClassroomSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from classes.models import Classroom
from django.contrib.auth.models import User
# Create your views here.
#----------------------------------API------------
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer



class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
    serializer_class = CreateClassroomSerializer
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(teacher=self.request.user)


class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassroomSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class DeleteClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
