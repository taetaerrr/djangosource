from django.urls import path, include
from .views import musician_create, musician_list, musician_edit

urlpatterns = [
    # http://127.0.0.1:8000/exam
    # http://127.0.0.1:8000/exam/musician/create/
    path("musician/create/", musician_create, name="musician_create"),
    path("musician/list/", musician_list, name="musician_list"),
    # http://127.0.0.1:8000/exam/musician/1/edit/
    path("musician/<int:id>/edit/", musician_edit, name="musician_edit"),
]