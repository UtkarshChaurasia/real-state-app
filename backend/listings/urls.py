from django.urls import path
from .views import ListingsView, SearchView, ListingDetailView

urlpatterns = [
    path('',ListingsView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>',ListingDetailView.as_view())
]