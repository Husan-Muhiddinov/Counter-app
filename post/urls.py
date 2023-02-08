from django.urls import path
from .views import BlogListView, Counter

urlpatterns=[
    path('',BlogListView.as_view(), name="index"),
    path('counter/<int:pk>', Counter, name="counter"),
]



