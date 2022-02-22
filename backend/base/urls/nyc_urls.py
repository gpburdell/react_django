from django.urls import path
from base.views import nyc_views as views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,

# )

urlpatterns = [

    path('cr1000/',views.cr1000, name="cr1000"),
    path('csi/',views.csi, name="csi"),
    path('ny17/',views.ny17, name="ny17"),
    # path('gage/<str:gage>/',views.ny17gage, name="ny17gage"),
    path('gage/',views.ny17gage, name="ny17gage"),
    path('onegage/<str:gage>/',views.ny17onegage, name="ny17onegage"),
]