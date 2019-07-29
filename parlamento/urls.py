from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register("", views.DipudatoView)

urlpatterns = [
    url('diputado', include(router.urls)),
]
