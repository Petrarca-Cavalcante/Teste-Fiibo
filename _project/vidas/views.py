from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from .serializers import VidaSerializer
from .models import Vida


class Vidas_View(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = VidaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request) -> Response: 
        vidas = Vida.objects.all()
        page = self.paginate_queryset(vidas, request)
        serializer = VidaSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def get_object(self, pk):
        try:
            return Vida.objects.get(pk=pk)
        except Vida.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, format=None):
        vida = self.get_object(pk)
        serializer = VidaSerializer(vida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vida = self.get_object(pk)
        vida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
