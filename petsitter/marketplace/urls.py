from django.urls import path
from . import views

urlpatterns = [
    path("sitters/", views.sitter_list),
    path("sitters/<int:pk>/", views.sitter_detail),
    path("pets/", views.pet_list),
    path("bookings/", views.booking_list),
]
