from django.urls import path

from . import views

app_name = "marketplace"

urlpatterns = [
    path("sitters/", views.SitterListView.as_view(), name="sitter-list"),
    path("sitters/<int:pk>/", views.SitterDetailView.as_view(), name="sitter-detail"),
    path("pets/", views.PetListCreateView.as_view(), name="pet-list"),
    path("bookings/", views.BookingListCreateView.as_view(), name="booking-list"),
    path("bookings/<int:pk>/", views.BookingDetailView.as_view(), name="booking-detail"),
]
