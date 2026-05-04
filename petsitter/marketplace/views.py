from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import SitterProfile, Pet, Booking
from .serializers import SitterProfileSerializer, PetSerializer, BookingSerializer


@api_view(["GET"])
def sitter_list(request):
    qs = SitterProfile.objects.all()
    city = request.query_params.get("city", "")
    service = request.query_params.get("service", "")
    if city:
        qs = qs.filter(city__icontains=city)
    if service:
        qs = qs.filter(services__service__name__icontains=service)
    return Response(SitterProfileSerializer(qs, many=True).data)


@api_view(["GET"])
def sitter_detail(request, pk):
    try:
        sitter = SitterProfile.objects.get(pk=pk)
    except SitterProfile.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    return Response(SitterProfileSerializer(sitter).data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def pet_list(request):
    if request.method == "GET":
        pets = Pet.objects.filter(owner=request.user)
        return Response(PetSerializer(pets, many=True).data)
    serializer = PetSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def booking_list(request):
    if request.method == "GET":
        bookings = Booking.objects.filter(owner=request.user)
        return Response(BookingSerializer(bookings, many=True).data)
    serializer = BookingSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
