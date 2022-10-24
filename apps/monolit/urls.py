from django.urls import path

from apps.monolit.views import HomePage

urlpatterns = [
    path('home/', HomePage.as_view())
]
