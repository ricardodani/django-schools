from rest_framework import serializers
from classroom.models import Quiz, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'first_name', 'email', 'date_joined'] 

class QuizSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Quiz
        fields = ['id', 'owner', 'name', 'subject']