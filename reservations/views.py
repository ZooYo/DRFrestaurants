from reservations.models import Reservation
from reservations.serializers import ReservationSerializer, ReservationUpdateSerializer


from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated


class UserReservationPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_object == request.user


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        basic_operations = ("create",)
        if self.action in basic_operations:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [UserReservationPermission, ]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT':
            serializer_class = ReservationUpdateSerializer

        return serializer_class

    def perform_create(self, serializer):
        kwargs = {
            'user_object': self.request.user
        }
        serializer.save(**kwargs)

    def perform_update(self, serializer):
        removed_field = serializer.validated_data.pop('user_object', None)
        serializer.save()

    def get_queryset(self):
        return Reservation.objects.all().filter(user_object=self.request.user)
