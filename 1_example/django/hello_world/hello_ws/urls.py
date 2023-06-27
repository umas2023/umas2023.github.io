from django.urls import path
from . import views
websocket_urlpatterns = [path("hello_ws",views.WebsocketTest.as_asgi())]


