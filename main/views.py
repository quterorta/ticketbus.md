from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.db.models import Count
from django.contrib.postgres.operations import UnaccentExtension
# Create your views here.


def main_page_view(request):
    start_city = StartCity.objects.filter(popular=True).order_by('title')
    end_city = EndCity.objects.filter(popular=True).order_by('title')
    empty_trip_selector = "Для поиска введите параметры поездки"
    popular_trip = PopularTrip.objects.all().order_by('-id')

    datetime_marker = datetime.now()
    time_marker = timezone.now().time()
    date_marker = datetime_marker.date().strftime("%Y-%m-%d")

    if request.method == 'POST':

        start_trip_city = request.POST['order_ticket_form_city_start_trip']
        end_trip_city = request.POST['order_ticket_form_city_end_trip']
        trip_date = request.POST['order_ticket_form_date_trip']
        qty_of_passengers = request.POST['order_ticket_form_qty_of_passengers']

        if date_marker == trip_date:
            trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date).\
                filter(journey_marker__city_start_trip__title=start_trip_city,
                       journey_marker__city_end_trip__title=end_trip_city,
                       journey_marker__active=True).\
                filter(time_trip__gt=time_marker).\
                order_by('time_trip').distinct()
        else:
            trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
                filter(journey_marker__city_start_trip__title=start_trip_city,
                       journey_marker__city_end_trip__title=end_trip_city,
                       journey_marker__active=True).\
                order_by('time_trip').distinct()
        if not trip_selector:
            empty_trip_selector = "Nu s-au găsit călătorii pentru solicitarea dvs. :("

        return render(request, 'main/main_page.html',
                      {'trip_date': trip_date, 'date_marker': date_marker, 'time_marker': time_marker,
                       'popular_trip': popular_trip, 'start_trip_city': start_trip_city, 'end_trip_city': end_trip_city,
                       'qty_of_passengers': qty_of_passengers, 'trip_selector': trip_selector,
                       'empty_trip_selector': empty_trip_selector, 'start_city': start_city, 'end_city': end_city})

    else:
        return render(request, 'main/main_page.html',
                      {'popular_trip': popular_trip, 'start_city': start_city, 'end_city': end_city,
                       'date_marker': date_marker})


def order_page_view(request, id, date, time, qty):

    journey_id = id
    qty_of_passengers = qty

    journey = Journey.objects.get(id=journey_id)
    total_price = journey.price * qty_of_passengers

    return render(request, 'main/order_page.html', {'journey': journey, 'total_price': total_price, 'qty_of_passengers': qty_of_passengers, 'date': date, 'time': time})


def make_order_view(request, id, date, time, qty):

    journey_id = id
    qty_of_passengers = qty

    journey = Journey.objects.get(id=journey_id)
    total_price = journey.price * qty_of_passengers

    if request.method == 'POST':

        new_order = Order()
        new_order.journey = journey
        new_order.date_of_journey = date
        new_order.time_of_journey = time
        new_order.phone = request.POST['checkout_order_form_phone']
        new_order.email = request.POST['checkout_order_form_email']

        if qty_of_passengers >= 1:
            new_order.passenger1_name = request.POST['checkout_order_form_passenger1_name']
            new_order.passenger1_second_name = request.POST['checkout_order_form_passenger1_second_name']
            new_order.passenger1_passport_type = request.POST['checkout_order_form_passenger1_passport_type']
            #new_order.passenger1_passport_info = request.POST['checkout_order_form_passenger1_passport_info']

        if qty_of_passengers >= 2:
            new_order.passenger2_name = request.POST['checkout_order_form_passenger2_name']
            new_order.passenger2_second_name = request.POST['checkout_order_form_passenger2_second_name']
            new_order.passenger2_passport_type = request.POST['checkout_order_form_passenger2_passport_type']
            new_order.passenger2_passport_info = request.POST['checkout_order_form_passenger2_passport_info']

        if qty_of_passengers >= 3:
            new_order.passenger3_name = request.POST['checkout_order_form_passenger3_name']
            new_order.passenger3_second_name = request.POST['checkout_order_form_passenger3_second_name']
            new_order.passenger3_passport_type = request.POST['checkout_order_form_passenger3_passport_type']
            new_order.passenger3_passport_info = request.POST['checkout_order_form_passenger3_passport_info']

        if qty_of_passengers >= 4:
            new_order.passenger4_name = request.POST['checkout_order_form_passenger4_name']
            new_order.passenger4_second_name = request.POST['checkout_order_form_passenger4_second_name']
            new_order.passenger4_passport_type = request.POST['checkout_order_form_passenger4_passport_type']
            new_order.passenger4_passport_info = request.POST['checkout_order_form_passenger4_passport_info']

        if qty_of_passengers >= 5:
            new_order.passenger5_name = request.POST['checkout_order_form_passenger5_name']
            new_order.passenger5_second_name = request.POST['checkout_order_form_passenger5_second_name']
            new_order.passenger5_passport_type = request.POST['checkout_order_form_passenger5_passport_type']
            new_order.passenger5_passport_info = request.POST['checkout_order_form_passenger5_passport_info']

        if qty_of_passengers >= 6:
            new_order.passenger6_name = request.POST['checkout_order_form_passenger6_name']
            new_order.passenger6_second_name = request.POST['checkout_order_form_passenger6_second_name']
            new_order.passenger6_passport_type = request.POST['checkout_order_form_passenger6_passport_type']
            new_order.passenger6_passport_info = request.POST['checkout_order_form_passenger6_passport_info']

        if qty_of_passengers >= 7:
            new_order.passenger7_name = request.POST['checkout_order_form_passenger7_name']
            new_order.passenger7_second_name = request.POST['checkout_order_form_passenger7_second_name']
            new_order.passenger7_passport_type = request.POST['checkout_order_form_passenger7_passport_type']
            new_order.passenger7_passport_info = request.POST['checkout_order_form_passenger7_passport_info']

        if qty_of_passengers >= 8:
            new_order.passenger8_name = request.POST['checkout_order_form_passenger8_name']
            new_order.passenger8_second_name = request.POST['checkout_order_form_passenger8_second_name']
            new_order.passenger8_passport_type = request.POST['checkout_order_form_passenger8_passport_type']
            new_order.passenger8_passport_info = request.POST['checkout_order_form_passenger8_passport_info']

        if qty_of_passengers >= 9:
            new_order.passenger9_name = request.POST['checkout_order_form_passenger9_name']
            new_order.passenger9_second_name = request.POST['checkout_order_form_passenger9_second_name']
            new_order.passenger9_passport_type = request.POST['checkout_order_form_passenger9_passport_type']
            new_order.passenger9_passport_info = request.POST['checkout_order_form_passenger9_passport_info']

        new_order.payment_type = request.POST['checkout_order_form_payment_type']
        new_order.total_price = journey.price * qty_of_passengers
        new_order.save()
        # qty_of_seats_new = journey.qty_of_seats - qty_of_passengers
        # if qty_of_seats_new == 0:
        #     Journey.objects.filter(id=journey_id).update(active=False)
        # Journey.objects.filter(id=journey_id).update(qty_of_seats=qty_of_seats_new)
        redirect_to = '/success/{}'.format(new_order.id)
        return HttpResponseRedirect(redirect_to)

    return render(request, 'main/checkout.html', {'journey': journey, 'total_price': total_price, 'qty_of_passengers': qty_of_passengers, 'date': date, 'time': time})


def success_view(request, order_id):

    return render(request, 'main/success_page.html', {'order_id': order_id})


def popular_trip_view(request, start_trip_city, end_trip_city):

    start_city = StartCity.objects.filter(popular=True).order_by('title')
    end_city = EndCity.objects.filter(popular=True).order_by('title')
    empty_trip_selector = "Nu s-au găsit călătorii pentru solicitarea dvs. :("
    popular_trip = PopularTrip.objects.all().order_by('-id')
    datetime_marker = datetime.now()
    time_marker = timezone.now().time()
    date_marker = datetime_marker.date().strftime("%Y-%m-%d")

    trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=date_marker). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            filter(time_trip__gt=time_marker). \
            order_by('time_trip').distinct()

    if request.method == 'POST':
        #redirect_to = ''
        #return HttpResponseRedirect(redirect_to, main_page_view(request))
        return main_page_view(request)

    return render(request, 'main/popular.html', {'start_trip_city': start_trip_city, 'end_trip_city': end_trip_city,
                                                 'time_marker': time_marker, 'date_marker': date_marker,
                                                 'start_city': start_city, 'end_city': end_city,
                                                 'empty_trip_selector': empty_trip_selector, 'popular_trip': popular_trip,
                                                 'trip_selector': trip_selector
                                                 })


def order_by_time_low_view(request, start_trip_city, end_trip_city, trip_date, qty_of_passengers):
    start_city = StartCity.objects.filter(popular=True).order_by('title')
    end_city = EndCity.objects.filter(popular=True).order_by('title')
    empty_trip_selector = "Nu s-au găsit călătorii pentru solicitarea dvs. :("
    popular_trip = PopularTrip.objects.all().order_by('-id')

    trip_selector = None

    start_trip_city = start_trip_city
    end_trip_city = end_trip_city
    trip_date = trip_date
    qty_of_passengers = qty_of_passengers

    datetime_marker = datetime.now()
    time_marker = timezone.now().time()
    date_marker = datetime_marker.date().strftime("%Y-%m-%d")

    if date_marker == trip_date:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            filter(time_trip__gt=time_marker). \
            order_by('time_trip').distinct()
    else:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            order_by('time_trip').distinct()

    if request.method == 'POST':
        return main_page_view(request)

    return render(request, 'main/main_page_order_by_time.html', {'start_trip_city': start_trip_city, 'end_trip_city': end_trip_city,
                                                 'time_marker': time_marker, 'date_marker': date_marker,
                                                 'start_city': start_city, 'end_city': end_city,
                                                 'empty_trip_selector': empty_trip_selector, 'popular_trip': popular_trip,
                                                 'trip_selector': trip_selector, 'trip_date': trip_date, 'qty_of_passengers': qty_of_passengers,
                                                 })


def order_by_time_hight_view(request, start_trip_city, end_trip_city, trip_date, qty_of_passengers):
    start_city = StartCity.objects.filter(popular=True).order_by('title')
    end_city = EndCity.objects.filter(popular=True).order_by('title')
    empty_trip_selector = "Nu s-au găsit călătorii pentru solicitarea dvs. :("
    popular_trip = PopularTrip.objects.all().order_by('-id')

    trip_selector = None

    start_trip_city = start_trip_city
    end_trip_city = end_trip_city
    trip_date = trip_date
    qty_of_passengers = qty_of_passengers

    datetime_marker = datetime.now()
    time_marker = timezone.now().time()
    date_marker = datetime_marker.date().strftime("%Y-%m-%d")

    if date_marker == trip_date:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            filter(time_trip__gt=time_marker). \
            order_by('-time_trip').distinct()
    else:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            order_by('-time_trip').distinct()

    if request.method == 'POST':
        return main_page_view(request)

    return render(request, 'main/main_page_order_by_time_hight.html', {'start_trip_city': start_trip_city, 'end_trip_city': end_trip_city,
                                                 'time_marker': time_marker, 'date_marker': date_marker,
                                                 'start_city': start_city, 'end_city': end_city,
                                                 'empty_trip_selector': empty_trip_selector, 'popular_trip': popular_trip,
                                                 'trip_selector': trip_selector, 'trip_date': trip_date, 'qty_of_passengers': qty_of_passengers,
                                                 })



def order_by_price_low_view(request, start_trip_city, end_trip_city, trip_date, qty_of_passengers):
    start_city = StartCity.objects.filter(popular=True).order_by('title')
    end_city = EndCity.objects.filter(popular=True).order_by('title')
    empty_trip_selector = "Nu s-au găsit călătorii pentru solicitarea dvs. :("
    popular_trip = PopularTrip.objects.all().order_by('-id')

    trip_selector = None

    start_trip_city = start_trip_city
    end_trip_city = end_trip_city
    trip_date = trip_date
    qty_of_passengers = qty_of_passengers

    datetime_marker = datetime.now()
    time_marker = timezone.now().time()
    date_marker = datetime_marker.date().strftime("%Y-%m-%d")

    if date_marker == trip_date:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            filter(time_trip__gt=time_marker). \
            order_by('journey_marker__price').distinct()
    else:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            order_by('journey_marker__price').distinct()

    if request.method == 'POST':
        return main_page_view(request)

    return render(request, 'main/main_page_order_by_price.html', {'start_trip_city': start_trip_city, 'end_trip_city': end_trip_city,
                                                 'time_marker': time_marker, 'date_marker': date_marker,
                                                 'start_city': start_city, 'end_city': end_city,
                                                 'empty_trip_selector': empty_trip_selector, 'popular_trip': popular_trip,
                                                 'trip_selector': trip_selector, 'trip_date': trip_date, 'qty_of_passengers': qty_of_passengers,
                                                 })


def order_by_price_hight_view(request, start_trip_city, end_trip_city, trip_date, qty_of_passengers):
    start_city = StartCity.objects.filter(popular=True).order_by('title')
    end_city = EndCity.objects.filter(popular=True).order_by('title')
    empty_trip_selector = "Nu s-au găsit călătorii pentru solicitarea dvs. :("
    popular_trip = PopularTrip.objects.all().order_by('-id')

    trip_selector = None

    start_trip_city = start_trip_city
    end_trip_city = end_trip_city
    trip_date = trip_date
    qty_of_passengers = qty_of_passengers

    datetime_marker = datetime.now()
    time_marker = timezone.now().time()
    date_marker = datetime_marker.date().strftime("%Y-%m-%d")

    if date_marker == trip_date:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            filter(time_trip__gt=time_marker). \
            order_by('-journey_marker__price').distinct()
    else:
        trip_selector = TimeTrip.objects.filter(journey_marker__date_trip__date=trip_date). \
            filter(journey_marker__city_start_trip__title=start_trip_city,
                   journey_marker__city_end_trip__title=end_trip_city,
                   journey_marker__active=True). \
            order_by('-journey_marker__price').distinct()

    if request.method == 'POST':
        return main_page_view(request)

    return render(request, 'main/main_page_order_by_price_hight.html', {'start_trip_city': start_trip_city, 'end_trip_city': end_trip_city,
                                                 'time_marker': time_marker, 'date_marker': date_marker,
                                                 'start_city': start_city, 'end_city': end_city,
                                                 'empty_trip_selector': empty_trip_selector, 'popular_trip': popular_trip,
                                                 'trip_selector': trip_selector, 'trip_date': trip_date, 'qty_of_passengers': qty_of_passengers,
                                                 })
