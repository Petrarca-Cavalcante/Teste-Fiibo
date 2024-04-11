from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .serializers import VidaSerializer
from .models import Vida


class Vidas_View(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = VidaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        vidas = Vida.objects.all().order_by("data_de_criacao")
        page = self.paginate_queryset(vidas, request)
        serializer = VidaSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class Vida_View(APIView):

    def get(self, request: Request, vida_id) -> Response:
        vida = get_object_or_404(Vida, id=vida_id)
        serializer = VidaSerializer(vida)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, vida_id: str):
        vida = get_object_or_404(Vida, id=vida_id)
        serializer = VidaSerializer(vida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vida_id: str):
        vida = get_object_or_404(Vida, id=vida_id)
        vida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
