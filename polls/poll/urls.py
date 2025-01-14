from django.urls import path
from . import views

app_name = "poll"

# path("경로",뷰,name="별칭") 
# 뷰 - 1) 함수형 뷰  2) 클래스 뷰 

urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path("",views.index,name="index"),

    # http://127.0.0.1:8000/polls/1 : 1번 질문 조회
    path("<int:question_id>/",views.detail, name="detail"),

    # http://127.0.0.1:8000/polls/1/vote : 1번 질문에 대한 답변 선택 
    path("<int:question_id>/vote/",views.vote, name="vote"),

    # http://127.0.0.1:8000/polls/1/results : 
    path("<int:question_id>/results/",views.results, name="results"),
]
