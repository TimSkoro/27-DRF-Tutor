from django.urls import path

from .views import CoinsListApi, CoinApi, CheckUser, AsRoot, CreateNewUser

urlpatterns = [
    path("coins_list/", CoinsListApi.as_view()),
    path("coin/<str:coin_id>/", CoinApi.as_view()),
    path("check/", CheckUser.as_view()),
    path("login_as_root/", AsRoot.as_view()),
    path("create_user/", CreateNewUser.as_view())
]
