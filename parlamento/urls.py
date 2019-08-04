from rest_framework import routers
from django.conf.urls import url, include
from .views import DipudatoView

router = routers.SimpleRouter()

# router = routers.DefaultRouter()
# router.register("", views.DipudatoView)

# urlpatterns = [
#     url('diputado', include(router.urls)),
# ]
router.register(r'diputados', DipudatoView)
urlpatterns = router.urls
