from django.shortcuts import render
from django.views.generic import View
from .models import Question
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home(LoginRequiredMixin, View):
    def get(self, request):
        questions = Question.objects.all()
        trending_questions = Question.objects.all().order_by('likes')[0:5]
        context = {
            'questions': questions,
            'trending': trending_questions
        }
        return render(request, 'forum/home.html', context)


class MyPosts(LoginRequiredMixin, View):
    def get(self, request):
        questions = Question.objects.filter(user=request.user)
        context = {
            'questions': questions,
        }
        return render(request, 'forum/my-posts.html', context)


class QuestionDetail(LoginRequiredMixin, View):
    def get(self, request, pk):
        question = get_object_or_404(Question, id=pk)
        context = {
            'question': question
        }
        return render(request, 'forum/question-detail.html', context)
