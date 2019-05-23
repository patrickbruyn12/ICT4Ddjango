from django.urls import path
from . import views

urlpatterns = [
    path("", views.voiceLabel, name="voiceLabel"),
    path("project_extra/", views.project_extra, name="project_extra"),
    path('project_extra/<int:pk>', views.project_extra, name="project_extra_withPK"),
]