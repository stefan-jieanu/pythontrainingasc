from rest_framework import generics, permissions

from .models import Booking, Pet, SitterProfile
from .serializers import BookingSerializer, PetSerializer, SitterProfileSerializer


class SitterListView(generics.ListAPIView):
    """
    GET /api/sitters/
    Filters:
      ?city=amsterdam   (case-insensitive contains)
      ?service=boarding (case-insensitive contains on service name)
      ?max_price=30     (only sitters offering at least one service at <= max_price)
    Public — no auth required.
    """

    serializer_class = SitterProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = (
            SitterProfile.objects.select_related("user")
            .prefetch_related("services__service")
            .all()
        )
        params = self.request.query_params

        city = params.get("city")
        if city:
            qs = qs.filter(city__icontains=city)

        service = params.get("service")
        if service:
            qs = qs.filter(services__service__name__icontains=service)

        max_price = params.get("max_price")
        if max_price:
            try:
                qs = qs.filter(services__price_per_day__lte=max_price)
            except (TypeError, ValueError):
                pass

        return qs.distinct()


class SitterDetailView(generics.RetrieveAPIView):
    """GET /api/sitters/<id>/"""

    queryset = SitterProfile.objects.select_related("user").prefetch_related(
        "services__service"
    )
    serializer_class = SitterProfileSerializer
    permission_classes = [permissions.AllowAny]


class PetListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/pets/  -> list current user's pets
    POST /api/pets/  -> create a pet (owner auto-assigned to request.user)
    """

    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user).order_by("name")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookingListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/bookings/  -> list current user's bookings
    POST /api/bookings/  -> create a booking (validates dates + pet ownership)
    """

    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Booking.objects.filter(owner=self.request.user)
            .select_related("sitter_service__service", "sitter_service__sitter__user")
            .prefetch_related("pets")
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookingDetailView(generics.RetrieveUpdateAPIView):
    """
    GET   /api/bookings/<id>/
    PATCH /api/bookings/<id>/  -> update status / notes (owner only for now)
    """

    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(owner=self.request.user)
