from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView
from classroom.serializers import QuizSerializer
from classroom.models import Quiz


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        elif request.user.is_student:
            return redirect('students:quiz_list')
        else:
            return redirect('admin:index')
    return render(request, 'classroom/home.html')


class QuizAPIView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer