from django.urls import path
from .views import Planos_view, Plano_View

urlpatterns = [
    path("planos", Planos_view.as_view()),
    path("plano/<int:plano_id>", Plano_View.as_view()),
]
