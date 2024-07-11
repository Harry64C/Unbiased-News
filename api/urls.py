from django.urls import path
from .views import main
from .views import RoomView

urlpatterns = [
    path('', main),
    path('home', RoomView.as_view()),
]
