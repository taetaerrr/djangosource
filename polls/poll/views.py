from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.views.generic.base import TemplateView
from .models import Question


class HomeView(TemplateView):
    template_name = "home.html"

# 함수형 뷰
# HttpResponse 객체 리턴 하거나
# render(request, 템플릿명) 리턴 
# redirect() 리턴 


def index(request):
    # return HttpResponse("Hello")

    # 전체 question 조회
    questions = Question.objects.all()

    return render(request, "poll/index.html",{"questions":questions})

def detail(request, question_id):
    # get() : 원하는 정보를 찾지 못하는 경우 DoesNotExist 발생

    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question id를 확인해 주세요")
    question = get_object_or_404(Question, id=question_id)
    return render(request, "poll/detail.html",{"question": question})

    

def vote(request, question_id):
    pass

def results(request, question_id):
    pass