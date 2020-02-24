from django.contrib.auth.models import User
from rest_framework import serializers
from classes.models import Classroom
from django.contrib.auth.models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","password","last_name","first_name"]
    def create (self, validated_data) :
        user = User(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])

        user.save()


        return validated_data

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject','name','year' , 'teacher']

class ClassroomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields ='__all__'
class UpdateClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['teacher']

class CreateClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['teacher']
