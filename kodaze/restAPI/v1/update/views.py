from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework import permissions

from restAPI.v1.update.serializers import UpdateSerializer
from update.models import Update

from restAPI.v1.update.filters import UpdateFilter


class UpdateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UpdateFilter
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Update əlavə edildi"}, status=status.HTTP_201_CREATED, headers=headers)


class UpdateDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UpdateFilter
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"detail": "Məlumatlar yeniləndi"})
