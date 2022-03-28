from django.urls import path
from base.views import danziger_views as views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,

# )

urlpatterns = [

   # path('gage/<str:gage>/',views.ny17gage, name="ny17gage"),
    # path('getCurrentData/',views.getCurrentData, name="getCurrentData"),
    # path('onegage/<str:gage>/',views.onegage, name="onegage"),
    path('gage/',views.gage, name="gage"),
    path('lifts/',views.lifts, name="lifts"),
]