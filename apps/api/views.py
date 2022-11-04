from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.serializers import CoinSerialize
from apps.common.utils import (
    get_coin_by_id, get_coins_list,
)


class IsNotOleg(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return request.user.username.lower() != "oleg"


class CoinsListApi(APIView):

    def get(self, request):
        coins_list = get_coins_list()
        return Response(coins_list, status=status.HTTP_204_NO_CONTENT)


class CoinApi(APIView):

    def get(self, request, coin_id):
        coin_data = get_coin_by_id(coin_id)
        ser = CoinSerialize(data=coin_data)
        ser.is_valid()
        return Response(ser.data)


class CheckUser(APIView):
    permission_classes = [IsAuthenticated, IsNotOleg]

    def get(self, request):
        current_user = request.user
        data = {
            "user": current_user.username
        }
        current_user.set_password("1234")
        current_user.save()

        return Response(data)


class CreateNewUser(APIView):
    def post(self, request):
        username = request.data.get('login')
        password = request.data.get('password')
        assert not User.objects.filter(username=username).exists()
        new_user = User.objects.create_user(username=username, password=password)
        login(request, new_user)
        return Response({
            "create": "new",
            "user": username
        })


class AsRoot(APIView):
    # def get(self, request):
    #     root = User.objects.filter(is_superuser=True).first()
    #     login(request, root)
    #     return Response({"you": "root"})

    def post(self, request):
        username = request.data.get('login')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            try:
                new_user = User.objects.create_user(username=username, password=password)
                login(request, new_user)
            except:
                raise AuthenticationFailed
        print(type(request.data))
        return Response('You make Post')

    def delete(self, request):
        logout(request)
        return Response("you logout")
