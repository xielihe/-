# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle

from .models import *
from .serializers import *
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.

class exploEviViewset(mixins.CreateModelMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取
    create:
        添加
    update:
        更新
    delete:
        删除
    """
    #queryset = exploSample.objects.filter(sname="样本3")
    #serializer_class = exploSampleSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
   # search_fields = ("sname", "sampleID", "user__name", "inputDate",)
    ordering_fields = ("sampleID", "inputDate",)
    def get_queryset(self):
        queryset = exploEvi.objects.all()
        sname = self.request.query_params.get("sname","")
        if sname:
            queryset = queryset.filter(sname__contains=sname)
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return exploEviDetailSerializer
        return exploEviSerializer
"""
    def perform_create(self, serializer):
        exploSample = serializer.save()
        shop_carts = exploSample.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            exploSampleFiles = exploSampleFile()
            exploSampleFiles.goods = shop_cart.goods
            exploSampleFiles.goods_num = shop_cart.nums
            exploSampleFiles.exploSample = exploSample
            order_goods.save()

            shop_cart.delete()
        return exploSample
"""


class exploEviFileViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = exploEviFile.objects.all()
    serializer_class = exploEviFileSerializer

class exploEviPeakViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = exploEviPeak.objects.all()
    serializer_class = exploEviPeakSerializer

class exploChEviViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = exploChEvi.objects.all()
    serializer_class = exploChEviSerializer

class devCompEviFileViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = devCompEviFile.objects.all()
    serializer_class = devCompEviFileSerializer

class devCompEviPeakViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = devCompEviPeak.objects.all()
    serializer_class = devCompEviPeakSerializer

class  devCompChEviViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = devCompChEvi.objects.all()
    serializer_class =  devCompChEviSerializer

class devCompEviViewset(mixins.CreateModelMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取
    create:
        添加
    update:
        更新
    delete:
        删除
    """
    #queryset = exploSample.objects.filter(sname="样本3")
    #serializer_class = exploSampleSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
   # search_fields = ("sname", "sampleID", "user__name", "inputDate",)
    ordering_fields = ("sampleID", "inputDate",)
    def get_queryset(self):
        queryset = devCompEvi.objects.all()
        sname = self.request.query_params.get("sname","")
        if sname:
            queryset = queryset.filter(sname__contains=sname)
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return devCompEviDetailSerializer
        return devCompEviSerializer

class devShapeEviViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = devShapeEvi.objects.all()
    serializer_class = devShapeEviSerializer
