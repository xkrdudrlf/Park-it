from django.db import models
from django.contrib.auth.models import AbstractUser

# USER MODELS
class CustomUser(AbstractUser):

    # blank = False means that the field cannot be left blank
    # null = True sets NULL on column in DB
    email = models.EmailField(unique=True, blank=False)
    phoneNumber = models.CharField(max_length=10, unique=True, blank=False)
    username = models.CharField(max_length=24, unique=True)

    def __str__(self) -> str:
        return self.name

class CardDetails(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    cardNumber = models.CharField(min_length=16, max_length=16, unique=True)
    expiryDate = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)

class BankDetails(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    BSB = models.CharField(max_length=6)
    accountNumber = models.CharField(max_length=10)
    accountName = models.CharField(max_length=100)

# CONSUMER MODELS
class Consumer(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    @classmethod
    def create(cls, user: CustomUser) -> 'Consumer':
        return cls(user=user)

class Vehicle(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    carMake = models.CharField(max_length=100)
    carModel = models.CharField(max_length=100)
    carYear = models.IntegerField()
    carColour = models.CharField(max_length=100)
    carRego = models.CharField(max_length=6, unique=True)

# PROVIDER MODELS
class Provider(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    @classmethod
    def create(cls, user: CustomUser) -> 'Provider':
        return cls(user=user)

class ParkingSpace(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    streetAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=3)
    postcode = models.CharField(max_length=4)

class Transaction(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE)
    parkingSpace = models.ForeignKey('ParkingSpace', on_delete=models.RESTRICT)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    totalCost = models.DecimalField(max_digits=6, decimal_places=2)

# REVIEW MODELS
class Review(models.Model):
    parkingSpace = models.ForeignKey('ParkingSpace', on_delete=models.CASCADE)
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    publishDate = models.DateTimeField(auto_now_add=True)