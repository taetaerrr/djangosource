from django.shortcuts import render, redirect
from .models import Todo


def todo_list(request):

    # Todo 전체 조회
    # todos = Todo.objects.all()

    # 완료되지 않은 할일 목록 추출
    todos = Todo.objects.filter(completed=False)
    return render(request, "todo/list.html", {"todos": todos})


def todo_detail(request, id):
    # Todo 상세 조회
    todo = Todo.objects.get(id=id)
    return render(request, "todo/detail.html", {"todo": todo})


def todo_register(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        important = request.POST.get("important")

        print(f"post {title},{description},{important}")

        if important:
            todo = Todo(title=title, description=description, important=True)
        else:
            todo = Todo(title=title, description=description)

        todo.save()
        return redirect("todo_list")
    else:
        return render(request, "todo/create.html")


def todo_edit(request, id):

    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        # 폼 안의 내용 개별로 가져오기
        title = request.POST.get("title")
        description = request.POST.get("description")
        important = request.POST.get("important")
        completed = request.POST.get("completed")

        print(f"post {title},{description},{important},{completed}")

        todo.title = title
        todo.description = description

        if important:
            todo.important = True
        else:
            todo.important = False

        if completed:
            todo.completed = True
        else:
            todo.completed = False

        todo.save()
        return redirect("todo_detail", id=todo.id)

    else:
        return render(request, "todo/edit.html", {"todo": todo})


def todo_done(request):
    # Todo 완료 목록 조회
    todos = Todo.objects.filter(completed=True)
    return render(request, "todo/done.html", {"todos": todos})
