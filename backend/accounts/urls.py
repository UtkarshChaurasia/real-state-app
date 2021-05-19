from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignupView

URLPattern = [
    path('signup', SignupView.as_view()),
]