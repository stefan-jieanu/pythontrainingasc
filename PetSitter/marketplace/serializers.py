from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Booking, Pet, Service, SitterProfile, SitterService


class UserMiniSerializer(serializers.ModelSerializer):
    """Minimal user info to embed inside a sitter response."""

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "full_name")

    def get_full_name(self, obj: User) -> str:
        return obj.get_full_name() or obj.username


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "description")


class SitterServiceSerializer(serializers.ModelSerializer):
    """A service offered by a sitter, with its price. Used nested in SitterProfile."""

    service = ServiceSerializer(read_only=True)

    class Meta:
        model = SitterService
        fields = ("id", "service", "price_per_day")


class SitterProfileSerializer(serializers.ModelSerializer):
    """Sitter with nested user info and the list of services they offer."""

    user = UserMiniSerializer(read_only=True)
    services = SitterServiceSerializer(many=True, read_only=True)

    class Meta:
        model = SitterProfile
        fields = ("id", "user", "bio", "city", "years_experience", "services")


class PetSerializer(serializers.ModelSerializer):
    species_display = serializers.CharField(source="get_species_display", read_only=True)

    class Meta:
        model = Pet
        # `owner` is read-only — set automatically from request.user in the view.
        fields = ("id", "owner", "name", "species", "species_display", "breed", "age")
        read_only_fields = ("owner",)


class BookingSerializer(serializers.ModelSerializer):
    num_days = serializers.IntegerField(read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Booking
        fields = (
            "id",
            "owner",
            "sitter_service",
            "pets",
            "start_date",
            "end_date",
            "status",
            "notes",
            "created_at",
            "num_days",
            "total_price",
        )
        read_only_fields = ("owner", "created_at")

    def validate(self, attrs):
        start = attrs.get("start_date")
        end = attrs.get("end_date")
        if start and end and end <= start:
            raise serializers.ValidationError(
                {"end_date": "end_date must be after start_date."}
            )
        return attrs

    def validate_pets(self, pets):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            raise serializers.ValidationError("Authentication required.")
        bad = [p for p in pets if p.owner_id != request.user.id]
        if bad:
            names = ", ".join(p.name for p in bad)
            raise serializers.ValidationError(
                f"These pets don't belong to you: {names}"
            )
        if not pets:
            raise serializers.ValidationError("A booking must include at least one pet.")
        return pets
