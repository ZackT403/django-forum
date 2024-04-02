from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Question, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePostForm, CreateCommentForm


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
        questions = Question.objects.filter(user=request.user).order_by('-pk')
        context = {
            'questions': questions,
        }
        return render(request, 'forum/my-posts.html', context)

    def post(self, request, *args, **kwargs):
        id = request.GET.get("id")
        question = Question.objects.get(id=id)
        if question.user == request.user:
            question.delete()

        return redirect('/myposts')
class QuestionDetail(LoginRequiredMixin, View):
    def get(self, request, pk):
        form = CreateCommentForm()
        question = get_object_or_404(Question, id=pk)
        comments = Comment.objects.filter(post__id=pk)
        context = {
            'question': question,
            'form': form,
            'comments': comments
        }
        return render(request, 'forum/question-detail.html', context)

    def post(self, request, pk):
        form = CreateCommentForm(data=request.POST)
        post = get_object_or_404(Question, id=pk)
        if form.is_valid():
            user = request.user
            content = form.data['content']
            Comment.objects.create(post=post, content=content)
            return redirect(f'/{pk}')
        context = {
            'question': post,
            'form': form
        }
        return render(request, 'forum/question-detail.html', context)

class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        form = CreatePostForm()
	context = {'form':form}
        return render(request, 'forum/create-post.html', context)

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.data['title']
            body = form.data['body']
            Question.objects.create(user=user, title=title, body=body)
            return redirect('/myposts')
        else:
	    context = {'form': form}
            return render(request, 'forum/create-post.html', context)

