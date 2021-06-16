from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    search_fields = ("city_start_trip", "city_end_trip", "city_center_trip", "all_city_trip", "type_of_transport", "model_of_transport", "id",)
    list_filter = ("active", "city_start_trip", "city_end_trip", "type_of_transport", "model_of_transport", "date_trip", "time_trip",)
    filter_horizontal = ("date_trip", "time_trip",)
    list_display = ('city_start_trip', 'city_end_trip', 'transfer', 'active', 'timpul', 'datele')
    list_display_links = ('city_start_trip', 'city_end_trip', 'transfer', 'active')

    def timpul(self, obj):
        return "\n".join(str(t.time_trip) for t in obj.time_trip.all())

    def datele(self, obj):
        return "\n".join(str(t.date) for t in obj.date_trip.all())


@admin.register(StartCity)
class StartCityAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("popular",)


@admin.register(EndCity)
class EndCityAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("popular",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("id",)
    list_filter = ("journey", "journey__date_trip", "journey__time_trip",)


@admin.register(DateMarker)
class DateMarkerAdmin(admin.ModelAdmin):
    list_display = ('date',)
    ordering = ('date',)


@admin.register(TimeTrip)
class TimeTripAdmin(admin.ModelAdmin):
    ordering = ('time_trip',)


@admin.register(PopularTrip)
class PopularTripAdmin(admin.ModelAdmin):
    search_fields = ("start_city_popular_trip", "end_city_popular_trip",)
    list_filter = ("start_city_popular_trip", "end_city_popular_trip", "active",)
    list_display = ("start_city_popular_trip", "end_city_popular_trip", "active",)
    list_display_links = ("start_city_popular_trip", "end_city_popular_trip", "active",)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    list_display_links = ('title',)
    ordering = ('title',)


@admin.register(ModelOfTransport)
class ModelOfTransportAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    list_display_links = ('title',)
    ordering = ('title',)
