from django.urls import path
from .views import Vidas_View, Vida_View

urlpatterns = [
    path("vidas", Vidas_View.as_view()),
    path("vida/<str:vida_id>", Vida_View.as_view()),
]
