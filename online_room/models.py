from django.db import models

# Create your models here.

ratings = [('1', '1'), 
           ('2', '2'), 
           ('3', '3'), 
           ('4', '4'), 
           ('5', '5')]

class User(models.Model):
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField(max_length=50)
    PASSWORD = models.CharField(max_length=10)
    PROFILE_PIC = models.ImageField(upload_to='user_profile_pics')

    def userprofilepics(self):
        return mark_safe('<img src="{}" width ="100px">'.format(self.PROFILE_PIC.url))

    def __str__(self):
        return self.EMAIL
    

class Country(models.Model):
    COUNTRY_NAME = models.CharField(max_length=50)

    def __str__(self):
        return self.COUNTRY_NAME

class State(models.Model):
    COUNTRY = models.ForeignKey(Country, on_delete=models.CASCADE)
    STATE_NAME = models.CharField(max_length=50)

    def __str__(self):
        return self.STATE_NAME

class City(models.Model):
    STATE = models.ForeignKey(State, on_delete=models.CASCADE)
    CITY_NAME = models.CharField(max_length=50)

    def __str__(self):
        return self.CITY_NAME

class HotelCategory(models.Model):
    CATEGORY_NAME = models.CharField(max_length=30)

    def __str__(self):
        return self.CATEGORY_NAME

class Hotel(models.Model):
    HOTEL_NAME = models.CharField(max_length=50)
    HOTEL_DESCRIPTION = models.TextField()
    HOTEL_CATEGORY = models.ForeignKey(HotelCategory, on_delete=models.CASCADE)
    LOCATION = models.CharField(max_length=50)
    CITY = models.ForeignKey(City, on_delete=models.CASCADE)
    PHONE = models.BigIntegerField()
    EMAIL = models.EmailField(max_length=50)
    ZIP_CODE = models.CharField(max_length=6)
    ADDEDAT = models.DateField()
    RATINGS = models.CharField(max_length=5, choices=ratings)
    NUMBER_REVIEWS = models.CharField(max_length=10)

    def __str__(self):
        return self.HOTEL_NAME

class Room(models.Model):
    HOTEL = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    NNAME = models.CharField(max_length=50)
    DESCRIPTION = models.TextField()
    PRICE_PER_NIGHT = models.IntegerField()
    NUM_BEDS = models.CharField(max_length=5, choices=ratings)
    CAPACITY = models.IntegerField()
    IS_AVAILABLE = models.IntegerField()
    CREATED_AT = models.DateField()
    
    def __str__(self):
        return self.NNAME

class RoomImages(models.Model):
    ROOM = models.ForeignKey(Room, on_delete=models.CASCADE)
    IMAGE = models.ImageField(upload_to='roomimage')

    def rimage(self):
        return mark_safe('<img src="{}" width ="100px">'.format(self.IMAGE.url))

    def __str__(self):
        return self.IMAGE

class Reviews(models.Model):
    HOTEL = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    RATING = models.CharField(max_length=5, choices=ratings)
    COMMENT = models.TextField()
    ADDED_AT = models.DateField()

    def __str__(self):
        return self.RATING

class Favorite(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    HOTEL = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Bookings(models.Model):
    USER = models.CharField(max_length=50)
    ROOM = models.ForeignKey(HotelCategory, on_delete=models.CASCADE)
    CHECK_IN_DATE = models.DateField()
    CHECK_OUT_DATE = models.ForeignKey(City, on_delete=models.CASCADE)
    NUM_ADULTS = models.IntegerField()
    NUM_CHILDREN = models.IntegerField()
    TOTAL_PRICE = models.FloatField()
    IS_CONFIRMED = models.CharField(max_length=5, choices=[('yes', 'YES'), ('no', 'NO')])
    CREATED_AT = models.DateField()

    def __str__(self):
        return self.IS_CONFIRMED

class Payments(models.Model):
    BOOKING = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    AMOUNT = models.FloatField()
    PAYMENT_DATE = models.DateField()
    PAYMENT_METHOD = models.CharField(max_length=50, choices=[('credit_card', 'Credit_card'), ('debit_card', 'Debit_card'), ('paypal', 'Paypal'), ('others', 'Other')])
    STATUS = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')

    def __str__(self):
        return self.STATUS