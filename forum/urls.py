from django.urls import path
from .views import Home, QuestionDetail, MyPosts, CreatePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('myposts/', MyPosts.as_view(), name='myposts'),
    path('create/', CreatePost.as_view(), name='createPost'),
    path('<int:pk>/', QuestionDetail.as_view(), name='detail')
]
