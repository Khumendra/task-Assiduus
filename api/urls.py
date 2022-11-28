from pprint import pprint

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'message', views.MessageViewSet, basename="message")
router.register(r'', views.GetMessageViewSet, basename="")

pprint(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.CustomAuthTokenLogin.as_view())
]
