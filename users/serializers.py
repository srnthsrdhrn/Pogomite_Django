from rest_framework import serializers

from users.models import User, Slider


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'mobile_number', 'address', 'profile_pic',
                  'mqtt_token', 'lat', 'lng', 'is_offering_service']

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class SliderSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Slider
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url
