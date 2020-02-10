from basic_restaurants.models import Restaurant
from basic_restaurants.serializers import RestaurantSerializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):

        if self.action == "list":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def list(self, request, **kwargs):
        users = Restaurant.objects.all()
        serializer = RestaurantSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
