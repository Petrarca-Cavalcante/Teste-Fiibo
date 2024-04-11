from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from .serializers import PlanoSerializer
from .models import Plano

class Planos_view(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = PlanoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        planos = Plano.objects.all().order_by("id")
        result_page = self.paginate_queryset(planos, request)
        serializer = PlanoSerializer(result_page, many=True)
        
        return self.get_paginated_response(serializer.data)


class Plano_View(APIView):
    def get(self, request: Request, plano_id: int) -> Response:
        plano = get_object_or_404(Plano, id=plano_id)
        serializer = PlanoSerializer(plano)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request: Request, plano_id: int) -> Response:
        plano = get_object_or_404(Plano, id=plano_id)
        serializer = PlanoSerializer(plano, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def delete(self, request: Request, plano_id: int) -> Response:
        plano = get_object_or_404(Plano, id=plano_id)
        plano.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
