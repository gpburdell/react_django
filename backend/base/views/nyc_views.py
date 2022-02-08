from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User

from base.models import Cr1000FtlaudMonitor, Ny17Table1
from django.core import serializers
from base.serializers import CR1000_Serializer

from rest_framework import status


@api_view(['GET'])
def cr1000(request):
    data = Cr1000FtlaudMonitor.objects.using('lndb').all()
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    serializer = CR1000_Serializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def csi(request):
    data = Cr1000FtlaudMonitor.objects.using('lndb').values('tmstamp','measure_avg')
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    # serializer = CR1000_Serializer(data, many=True)
    context = {
    'tmstamp': [i['tmstamp'] for i in data],
    'measure_avg': [i['measure_avg'] for i in data]
    }
    #print(context)
    return Response(context)

@api_view(['GET'])
def ny17(request):
    data = Ny17Table1.objects.using('lndb').values('tmstamp','laser_18_avg')
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    # serializer = CR1000_Serializer(data, many=True)
    context = {
    'tmstamp': [i['tmstamp'] for i in data],
    'laser_18_avg': [i['laser_18_avg'] for i in data]
    }
    #print(context)
    return Response(context)

@api_view(['GET'])
def ny17gage(request,gage):
    data = Ny17Table1.objects.using('lndb').values('tmstamp',gage)
    # data = serializers.serialize("json", Cr1000FtlaudMonitor.objects.using('lndb').all(), fields = ("tmstamp", "recnum", "measure_avg","ptemp"))
    # serializer = CR1000_Serializer(data, many=True)
    context = {
    'x': [i['tmstamp'] for i in data],
    'y': [i[gage] for i in data]
    }
    #print(context)
    return Response(context)