# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from service.models import Service, Order
from service.serializers import ServiceSerializer, OrderSerializer


# Create your views here.


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    # permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        datas = dict(request.query_params)
        temp = {}
        for data in datas:
            t = datas[data]
            temp[data] = t[0]
        queryset = self.queryset.filter(**temp)
        return Response(self.serializer_class(queryset, many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(request.data):
            serializer.create(serializer.validated_data)
            return Response({"Success"})
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if pk:
            return Response(self.serializer_class(self.queryset.filter(id=pk)))
        else:
            return Response({"No Primary Key Specified"})

    def destroy(self, request, pk=None, *args, **kwargs):
        if pk:
            service = self.queryset.filter(id=pk)
            service.delete()
            return Response({"Successfully Deleted Object"})
        return Response({"Bad Request"})


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        datas = dict(request.query_params)
        temp = {}
        for data in datas:
            t = datas[data]
            temp[data] = t[0]
        queryset = self.queryset.filter(**temp)
        return Response(self.serializer_class(queryset, many=True).data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if pk:
            return Response(self.serializer_class(self.queryset.filter(id=pk)))
        else:
            return Response({"No Primary Key Specified"})

    def destroy(self, request, pk=None, *args, **kwargs):
        if pk:
            service = self.queryset.filter(id=pk)
            service.delete()
            return Response({"Successfully Deleted Object"})
        return Response({"Bad Request"})


class CreateOrder(APIView):
    def post(self, request):
        data = request.data
        worker_id = data.get("worker_id")
        customer_id = data.get("customer_id")
        services = data.get("services")
        startDateTime = data.get("startDateTime")
        startDateTime = parse_datetime(startDateTime)
        try:
            order = Order.objects.get(worker_id=worker_id, customer_id=customer_id, startDateTime=startDateTime)
        except Order.DoesNotExist:
            order = Order.objects.create(worker_id=worker_id, customer_id=customer_id, startDateTime=startDateTime)
        for service_id in services:
            service = Service.objects.get(id=service_id)
            order.service.add(service)
        return Response({"status": "Success", "message": "Order Placed", "order_id": order.id})
