from django.urls import path

from .views import CoinsListApi, CoinApi

urlpatterns = [
    path("coins_list/", CoinsListApi.as_view()),
    path("coin/<str:coin_id>/", CoinApi.as_view()),
]
