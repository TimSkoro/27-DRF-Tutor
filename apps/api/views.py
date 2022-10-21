from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.serializers import CoinSerialize
from apps.common.utils import (
    get_coin_by_id, get_coins_list,
)


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
