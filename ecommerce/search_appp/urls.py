from django.urls import path
from . import views

app_name='search_appp'
urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]