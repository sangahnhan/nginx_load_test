from django.urls import path

from records.views import *

urlpatterns = [
    path('recordings', CreateView.as_view()),
]