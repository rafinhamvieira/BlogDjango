from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic import detail

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]