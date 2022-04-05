# "Queries" for Django database
from urllib import request
from users.forms import *
from users.models import CustomUser, ParkingSpace, Transaction
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
import datetime as dt
from drf_spectacular.utils import extend_schema

# Create your views here.
# @login_required(login_url='http://127.0.0.1:8000/')

# Users

class RemoveUserView(GenericAPIView):
    serializer_class = RemoveUserSerializer

    def delete(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        if not serializer.errors:
            serializer.delete(request)
            return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'User not deleted'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# PARKING SPACES

# Create a parking space

class CreateParkingSpace(CreateAPIView):
    serializer_class = ParkingSpaceSerializer
    queryset = ParkingSpace.objects.all()

# Do stuff with an existing parking space

class ParkingSpaceView(RetrieveUpdateDestroyAPIView):
    serializer_class = ParkingSpaceSerializer
    def get_queryset(self):
        space = self.kwargs['parkingID']
        return ParkingSpace.objects.filter(parkingSpace=space)

# Get all parking spaces owned by the user

class ParkingSpaceList(ListAPIView):
    serializer_class = ParkingSpaceSerializer
    def get_queryset(self):
        provider = self.request.user
        return ParkingSpace.objects.filter(provider=provider)

# IMAGES
       
# Upload an image
class CreateImage(CreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

# Do stuff with an existing image

class ImageView(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    def get_queryset(self):
        image = self.kwargs['imgID']
        return Image.objects.filter(pk=image)


# Get all images associated with a Parking Space

class ImageList(ListAPIView):
    serializer_class = ImageSerializer
    def get_queryset(self):
        space = self.kwargs['parkingID']
        return Image.objects.filter(parkingSpace=space)


# BOOKINGS
       
# Add a booking
class CreateBooking(CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

# Do stuff with an existing booking

class BookingView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        booking = self.kwargs['bookingID']
        return Transaction.objects.filter(pk=booking)


# Get all bookings associated with a Parking Space

class BookingList(ListAPIView):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        space = self.kwargs['parkingID']
        return Transaction.objects.filter(parkingSpace=space)

# Get all bookings that involve the user as a Provider

class ProviderBookingHistory(ListAPIView):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(provider=user)

# Get all bookings that involve the user as a Consumer   

class ConsumerBookingHistory(ListAPIView):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(consumer=user)


# FAVOURITE
       
# Favourite a parking space
class CreateFavourite(CreateAPIView):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()

# Do stuff with an existing Favourite

class FavouriteView(RetrieveUpdateDestroyAPIView):
    serializer_class = FavouriteSerializer
    def get_queryset(self):
        favourite = self.kwargs['favID']
        return Favourite.objects.filter(pk=favourite)

# Get all favourites associated with a Parking Space

class FavouriteList(ListAPIView):
    serializer_class = FavouriteSerializer
    def get_queryset(self):
        space = self.kwargs['parkingID']
        return Favourite.objects.filter(parkingSpace=space)

# VEHICLE

# Add a vehicle
class CreateVehicle(CreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

# Do stuff with an existing vehicle

class VehicleView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    def get_queryset(self):
        vehicle = self.kwargs['vehicleID']
        return Vehicle.objects.filter(pk=vehicle)

# Get all vehicles associated with a consumer

class VehicleList(ListAPIView):
    serializer_class = VehicleSerializer
    def get_queryset(self):
        owner = self.kwargs['consumerID']
        return Vehicle.objects.filter(user=owner)


# REVIEW

# Add a review

class CreateReview(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


# Do stuff with an existing review

class ReviewView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        review = self.kwargs['reviewID']
        return Review.objects.filter(pk=review)

# Get all reviews associated with a parking space

class ReviewList(ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        space = self.kwargs['parkingID']
        return Review.objects.filter(parkingSpace=space)



    

    
    
