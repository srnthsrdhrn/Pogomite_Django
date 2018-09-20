from rest_framework import serializers

from service.models import Service, Order
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = Service
        fields = ['type', 'name', 'description', 'fare', 'user', 'user_id', 'id']


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True)
    service = ServiceSerializer(read_only=True,many=True)
    worker = UserSerializer(read_only=True)
    worker_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']
