from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):

        if self.action == "list":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        kwargs = {
            'user': self.request.user
        }
        serializer.save(**kwargs)


