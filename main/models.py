from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import datetime
from django.utils import timezone


class TimeTrip(models.Model):

    time_trip = models.TimeField(verbose_name='Время')

    def __str__(self):
        return "{}".format(self.time_trip)


    class Meta:
        verbose_name = 'Timp'
        verbose_name_plural = 'Timpul'


class DateMarker(models.Model):

    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return "{}".format(self.date.strftime("%Y-%m-%d"))

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Datele'


class Journey(models.Model):

    city_start_trip = models.ForeignKey('StartCity', verbose_name='Punct de plecare', on_delete=models.CASCADE)
    city_end_trip = models.ForeignKey('EndCity', verbose_name='Punct de sosire', on_delete=models.CASCADE)
    city_center_trip = models.CharField(max_length=255, verbose_name='Oraș intermediar')
    all_city_trip = models.TextField(max_length=255, verbose_name='Toate orașele călătoresc')
    date_trip = models.ManyToManyField(DateMarker, verbose_name='Data plecării', related_name='journey_date_marker')
    time_trip = models.ManyToManyField(TimeTrip, verbose_name='Timp de plecare', related_name='journey_marker')
    time_in_journey = models.CharField(max_length=255, verbose_name='Timp de calatorie', null=True, blank=True)
    type_of_transport = models.CharField(max_length=255, choices=[('Autocar', 'Autocar'), ('Microbuze', 'Microbuze')], verbose_name='Tipul de transport')
    model_of_transport = models.ForeignKey('ModelOfTransport', verbose_name='Model de transport', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Prețul biletului')
    image = models.ImageField(verbose_name='Imagine', null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='Activ')
    transfer = models.ForeignKey('Transfer', verbose_name='Transportator', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} | {} | Activ:{}".format(self.city_start_trip, self.city_end_trip, self.model_of_transport, self.active)

    class Meta:
        verbose_name = 'Calatoria'
        verbose_name_plural = 'Traseu'


class StartCity(models.Model):

    title = models.CharField(max_length=255, verbose_name='Numele orasului')
    popular = models.BooleanField(default=True, verbose_name='Alesul')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Punct de plecare'
        verbose_name_plural = 'Puncte de plecare'


class EndCity(models.Model):
    title = models.CharField(max_length=255, verbose_name='Numele orasului')
    popular = models.BooleanField(default=True, verbose_name='Alesul')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Punct de sosire'
        verbose_name_plural = 'Puncte de sosire'


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in progress'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Comandă nouă'),
        (STATUS_COMPLETED, 'Achitat'),
    )

    PAYMENT_TYPE_CARD = 'card'
    PAYMENT_TYPE_TERMINAL = 'terminal'

    PAYMENT_TYPE_CHOICES = (
        (PAYMENT_TYPE_CARD, 'Plata cu cardul'),
        (PAYMENT_TYPE_TERMINAL, 'Plata prin terminal Cash'),
    )

    journey = models.ForeignKey('Journey', verbose_name='Calatoria', on_delete=models.CASCADE)
    date_of_journey = models.DateField(verbose_name='Data călătoriei', null=True, blank=True)
    time_of_journey = models.TimeField(verbose_name='Timp de calatorie', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Număr de telefon')
    email = models.CharField(max_length=255, verbose_name='E-mail')
    passenger1_name = models.CharField(max_length=255, verbose_name='Numele primului pasager')
    passenger1_second_name = models.CharField(max_length=255, verbose_name='Numele primului pasager')
    passenger1_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')], verbose_name='Tipul pașaportului')
    #passenger1_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger2_name = models.CharField(max_length=255, verbose_name='Al doilea nume pasager', null=True, blank=True)
    passenger2_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al doilea pasager', null=True, blank=True)
    passenger2_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger2_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger3_name = models.CharField(max_length=255, verbose_name='Al treilea nume al pasagerului', null=True, blank=True)
    passenger3_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al treilea pasager', null=True, blank=True)
    passenger3_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger3_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger4_name = models.CharField(max_length=255, verbose_name='Numele celui de-al patrulea pasager', null=True, blank=True)
    passenger4_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al patrulea pasager', null=True, blank=True)
    passenger4_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger4_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger5_name = models.CharField(max_length=255, verbose_name='Numele celui de-al cincilea pasager', null=True, blank=True)
    passenger5_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al cincilea pasager', null=True, blank=True)
    passenger5_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger5_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger6_name = models.CharField(max_length=255, verbose_name='Numele celui de-al șaselea pasager', null=True, blank=True)
    passenger6_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al șaselea pasager', null=True, blank=True)
    passenger6_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger6_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger7_name = models.CharField(max_length=255, verbose_name='Numele celui de-al șaptelea pasager', null=True, blank=True)
    passenger7_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al șaptelea pasager', null=True, blank=True)
    passenger7_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger7_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger8_name = models.CharField(max_length=255, verbose_name='Numele celui de-al optulea pasager', null=True, blank=True)
    passenger8_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al optulea pasager', null=True, blank=True)
    passenger8_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger8_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    passenger9_name = models.CharField(max_length=255, verbose_name='Numele celui de-al nouălea pasager', null=True, blank=True)
    passenger9_second_name = models.CharField(max_length=255, verbose_name='Numele celui de-al nouălea pasager', null=True, blank=True)
    passenger9_passport_type = models.CharField(max_length=255, choices=[('EU', 'EU'), ('MD', 'MD')],
                                                verbose_name='Tipul pașaportului', null=True, blank=True)
    #passenger9_passport_info = models.CharField(max_length=255, verbose_name='Seria și numărul pașaportului', null=True, blank=True)

    total_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Cost total')
    status = models.CharField(max_length=100, verbose_name='Stare', choices=STATUS_CHOICES, default=STATUS_NEW)
    payment_type = models.CharField(max_length=100, verbose_name='Modalitate de plată', choices=PAYMENT_TYPE_CHOICES, default=PAYMENT_TYPE_CARD)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Data creării comenzii')


    def __str__(self):
        return "#{}. Ordin de deplasare: {} - {} | {}, {} | {}. Creat de: {}".format(self.id, self.journey.city_start_trip, self.journey.city_end_trip, self.date_of_journey, self.time_of_journey, self.journey.model_of_transport, self.created_at.replace(microsecond=False, tzinfo=None))

    class Meta:
        verbose_name = 'Ordin'
        verbose_name_plural = 'Comenzi'


class PopularTrip(models.Model):

    start_city_popular_trip = models.ForeignKey('StartCity', verbose_name='Plecare', on_delete=models.CASCADE)
    end_city_popular_trip = models.ForeignKey('EndCity', verbose_name='Sosire', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagine', null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='Activ')

    def __str__(self):
        return "{} --- {} | {}".format(self.start_city_popular_trip, self.end_city_popular_trip, self.active)

    class Meta:
        verbose_name = 'Traseu popular'
        verbose_name_plural = 'Trasee populare'


class Transfer(models.Model):
    title = models.CharField(max_length=255, verbose_name='Transportator')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Transportator'
        verbose_name_plural = 'Transportatori'


class ModelOfTransport(models.Model):
    title = models.CharField(max_length=255, verbose_name='Model de transport')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Model de transport'
        verbose_name_plural = 'Modele de transport'