# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hashlib import sha256

# Create your views here.
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User, Slider
from users.serializers import UserSerializer, SliderSerializer


class LoginAPI(APIView):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return Response(UserSerializer(user).data)
                else:
                    return Response({"error": "Username or Password Wrong"})
            except User.DoesNotExist, e:
                return Response({"error": "User Does not Exist"})
        return Response({"error": "Bad Request Missing Parameters"}, status=400)


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            token = sha256(user.email).hexdigest()
            user.mqtt_token = token
            user.set_password(request.POST.get("password"))
            user.save()
            return Response({"Success": "User Created"})
        else:
            return Response(serializer.errors, status=400)


class SlideListAPI(APIView):
    def get(self, request):
        serializer = SliderSerializer(Slider.objects.all(), many=True)
        return Response(serializer.data)


class SaveSettings(APIView):
    authentication_classes = (BasicAuthentication,)

    def post(self, request):
        data = request.data
        user_id = data.get("user_id")
        is_offering_service = data.get("offer_service")
        user = User.objects.get(id=user_id)
        user.is_offering_service = is_offering_service
        user.save()
        return Response({"status": "Sucess"})
