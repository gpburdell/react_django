from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cr1000FtlaudMonitor
from .models import Ny17Table1
from django.core import serializers
from .serializers import Product,UserSerializer,UserSerializerWithToken, CR1000_Serializer, ProductSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
    #     token['message'] = 'hello world'

    #     return token
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET',])
def getRoutes(request):
    return Response("routes")

@api_view(['GET',])
def getUserProfile(request):
    user = request.user


    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET',])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

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
    'tmstamp': [i['tmstamp'] for i in data],
    'gage': [i[gage] for i in data]
    }
    #print(context)
    return Response(context)