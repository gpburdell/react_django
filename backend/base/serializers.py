from lib2to3.pytree import Base
from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Product, User, Cr1000FtlaudMonitor
from rest_framework_simplejwt.tokens import RefreshToken
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CR1000_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cr1000FtlaudMonitor
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id','username','email','name','isAdmin','groups']

    def get__id(self,obj):
        return obj.id

    def get_isAdmin(self,obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def get_groups(self, obj):
        return obj.groups.values_list('name', flat=True)

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id','username','email','name','isAdmin','token','groups']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)