from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


class SitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sitter_profile")
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    years_experience = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["city", "user__username"]

    def __str__(self) -> str:
        name = self.user.get_full_name() or self.user.username
        return f"{name} — {self.city}"


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class SitterService(models.Model):
    sitter = models.ForeignKey(
        SitterProfile,
        on_delete=models.CASCADE,
        related_name="services",
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sitter", "service"],
                name="unique_sitter_per_service",
            ),
        ]
        ordering = ["sitter", "service"]

    def __str__(self) -> str:
        name = self.sitter.user.get_full_name() or self.sitter.user.username
        return f"{name} — {self.service.name} (${self.price_per_day}/day)"


class Pet(models.Model):
    class Species(models.TextChoices):
        DOG = "dog", "Dog"
        CAT = "cat", "Cat"
        BIRD = "bird", "Bird"
        OTHER = "other", "Other"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=Species)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ["owner", "name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.get_species_display()})"


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    sitter_service = models.ForeignKey(
        SitterService,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    pets = models.ManyToManyField(Pet, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.PENDING,
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Booking {self.pk} ({self.status})"

    @property
    def num_days(self) -> int:
        days = (self.end_date - self.start_date).days
        return days if days > 0 else 1

    @property
    def total_price(self) -> Decimal:
        return self.sitter_service.price_per_day * self.num_days
