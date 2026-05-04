from rest_framework import serializers
from .models import SitterProfile, SitterService, Service, Pet, Booking


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "description")


class SitterServiceSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service.name", read_only=True)

    class Meta:
        model = SitterService
        fields = ("id", "service_name", "price_per_day")


class SitterProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    full_name = serializers.CharField(source="user.get_full_name", read_only=True)
    services = SitterServiceSerializer(many=True, read_only=True)

    class Meta:
        model = SitterProfile
        fields = ("id", "username", "full_name", "bio", "city", "years_experience", "services")


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("id", "name", "species", "breed", "age")

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)


class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    num_days = serializers.IntegerField(read_only=True)

    class Meta:
        model = Booking
        fields = ("id", "sitter_service", "pets", "start_date", "end_date", "status", "notes", "created_at", "num_days", "total_price")
        read_only_fields = ("status", "created_at")

    def validate(self, data):
        if data["end_date"] <= data["start_date"]:
            raise serializers.ValidationError("end_date must be after start_date.")
        request = self.context["request"]
        for pet in data["pets"]:
            if pet.owner != request.user:
                raise serializers.ValidationError(f"Pet '{pet.name}' does not belong to you.")
        return data

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
