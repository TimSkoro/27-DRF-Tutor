from django.urls import path

from apps.monolit.views import HomePage, NewsPage, ContactPage

urlpatterns = [
    path('home/', HomePage.as_view()),
    path('news/', NewsPage.as_view()),
    path('contact/', ContactPage.as_view())
]
