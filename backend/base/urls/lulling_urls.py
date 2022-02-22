from django.urls import path
from base.views import lulling_views as views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,

# )

urlpatterns = [

   # path('gage/<str:gage>/',views.ny17gage, name="ny17gage"),
    path('gage/',views.gage, name="ngage"),
    path('onegage/<str:gage>/',views.onegage, name="onegage"),
]