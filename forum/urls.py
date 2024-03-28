from django.urls import path
from .views import Home, QuestionDetail, MyPosts

urlpatterns = [
    path('', Home.as_view()),
    path('myposts/', MyPosts.as_view(), name='myposts'),
    path('<int:pk>/', QuestionDetail.as_view())
]
