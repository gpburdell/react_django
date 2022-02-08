from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,

# )

urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('',views.getRoutes, name="routes"),

    path('users/profile/',views.getUserProfile, name="user-profile"),
    path('users/',views.getUsers, name="users"),
    path('users/register/',views.registerUser, name='register'),

    path('products/',views.getProducts, name="products"),
    path('products/<str:pk>/',views.getProduct, name="product"),
    path('cr1000/',views.cr1000, name="cr1000"),
    path('csi/',views.csi, name="csi"),
    path('ny17/',views.ny17, name="ny17"),
    path('ny17gage/<str:gage>/',views.ny17gage, name="ny17gage"),
]