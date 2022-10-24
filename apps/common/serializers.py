from rest_framework import serializers


class CoinSerialize(serializers.Serializer):
    id = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    price = serializers.SerializerMethodField()

    # market_data = serializers.JSONField()
    # price = serializers.FloatField(source='market_data.current_price.usd')
    # random_number = serializers.SerializerMethodField()

    def get_price(self, obj):
        return self.initial_data.get('market_data').get('current_price').get('usd')

    # def get_random_number(self, obj):
    #     return random.random()
