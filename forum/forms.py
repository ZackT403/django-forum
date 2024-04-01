from django.forms import ModelForm
from .models import Question, Comment


class CreatePostForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
