from django.contrib import admin

from .models import Booking, Pet, Service, SitterProfile, SitterService


@admin.register(SitterProfile)
class SitterProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "years_experience")
    search_fields = ("city", "user__username", "user__first_name", "user__last_name", "bio")
    raw_id_fields = ("user",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")


@admin.register(SitterService)
class SitterServiceAdmin(admin.ModelAdmin):
    list_display = ("sitter", "service", "price_per_day")
    list_filter = ("service",)
    search_fields = ("sitter__user__username", "service__name")
    raw_id_fields = ("sitter", "service")


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "owner", "age")
    list_filter = ("species",)
    search_fields = ("name", "breed", "owner__username")
    raw_id_fields = ("owner",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "sitter_service", "start_date", "end_date", "status", "created_at")
    list_filter = ("status", "start_date")
    search_fields = ("owner__username", "notes")
    filter_horizontal = ("pets",)
    raw_id_fields = ("owner", "sitter_service")
