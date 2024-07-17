from django.contrib import admin
from .models import User, Country, State, City, HotelCategory, Hotel, Room, RoomImages, Reviews, Favorite, Bookings, Payments

# Register your models here.

@admin.register(User)
class DisplayUser(admin.ModelAdmin):
    list_display = ['FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PASSWORD', 'userprofilepics']

@admin.register(Country)
class DisplayCountry(admin.ModelAdmin):
    list_display = ['COUNTRY_NAME']

@admin.register(State)
class DisplayState(admin.ModelAdmin):
    list_display = ['COUNTRY', 'STATE_NAME']

@admin.register(City)
class DisplayCity(admin.ModelAdmin):
    list_display = ['STATE', 'CITY_NAME']

@admin.register(HotelCategory)
class DisplayHC(admin.ModelAdmin):
    list_display = ['CATEGORY_NAME']

@admin.register(Hotel)
class DisplayHotel(admin.ModelAdmin):
    list_display = ['HOTEL_NAME', 'HOTEL_DESCRIPTION', 'HOTEL_CATEGORY', 'LOCATION', 'CITY', 'PHONE', 'EMAIL', 'ZIP_CODE', 'ADDEDAT', 'RATINGS', 'NUMBER_REVIEWS']

@admin.register(Room)
class DisplayRoom(admin.ModelAdmin):
    list_display = ['HOTEL', 'NNAME', 'DESCRIPTION', 'PRICE_PER_NIGHT', 'NUM_BEDS', 'CAPACITY', 'IS_AVAILABLE', 'CREATED_AT']

@admin.register(RoomImages)
class DisplayRI(admin.ModelAdmin):
    list_display = ['ROOM', 'rimage']

@admin.register(Reviews)
class DisplayReviews(admin.ModelAdmin):
    list_display = ['HOTEL', 'USER', 'RATING', 'COMMENT', 'ADDED_AT']

@admin.register(Favorite)
class DisplayFavorite(admin.ModelAdmin):
    list_display = ['USER', 'HOTEL']

@admin.register(Bookings)
class DisplayBookings(admin.ModelAdmin):
    list_display = ['USER', 'ROOM', 'CHECK_IN_DATE', 'CHECK_OUT_DATE', 'NUM_ADULTS', 'NUM_CHILDREN', 'TOTAL_PRICE', 'IS_CONFIRMED', 'CREATED_AT']

@admin.register(Payments)
class DisplayPay(admin.ModelAdmin):
    list_display = ['BOOKING', 'AMOUNT', 'PAYMENT_DATE', 'PAYMENT_METHOD', 'STATUS']