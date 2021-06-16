from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main_page_view, name="home"),
    path('order/<int:id>/<str:date>/<str:time>/<int:qty>', order_page_view, name="order"),
    path('checkout/<int:id>/<str:date>/<str:time>/<int:qty>', make_order_view, name="checkout"),
    path('success/<int:order_id>', success_view, name="success"),
    path('popular/<str:start_trip_city>/<str:end_trip_city>', popular_trip_view, name="test"),
    path('search/<str:start_trip_city>/<str:end_trip_city>/<str:trip_date>/<int:qty_of_passengers>/order_by_time_low', order_by_time_low_view, name="order_by_time_low"),
    path('search/<str:start_trip_city>/<str:end_trip_city>/<str:trip_date>/<int:qty_of_passengers>/order_by_price_low', order_by_price_low_view, name="order_by_price_low"),
    path('search/<str:start_trip_city>/<str:end_trip_city>/<str:trip_date>/<int:qty_of_passengers>/order_by_time_hight', order_by_time_hight_view, name="order_by_time_hight"),
    path('search/<str:start_trip_city>/<str:end_trip_city>/<str:trip_date>/<int:qty_of_passengers>/order_by_price_hight', order_by_price_hight_view, name="order_by_price_hight"),
]