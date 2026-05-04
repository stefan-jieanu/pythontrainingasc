from django.contrib import admin
from .models import SitterProfile, Service, SitterService, Pet, Booking


@admin.register(SitterProfile)
class SitterProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "years_experience")
    search_fields = ("user__username", "city")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(SitterService)
class SitterServiceAdmin(admin.ModelAdmin):
    list_display = ("sitter", "service", "price_per_day")
    search_fields = ("sitter__user__username", "service__name")


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "breed", "age", "owner")
    search_fields = ("name", "owner__username")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("owner", "sitter_service", "start_date", "end_date", "status")
    search_fields = ("owner__username",)
