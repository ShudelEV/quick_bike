from django.db import models
from Profile.models import User

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address


def photo_path_company(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<name>/
    return 'company_{0}/{1}'.format(instance.name, filename)


class Company(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(verbose_name="company photo", blank=True,
                              max_length=255, upload_to=photo_path_company)
    contact_info = models.ForeignKey(ContactInfo)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


def photo_path_shop(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<name>/shop_<name>/
    parent_path = instance.company._meta.get_field('photo').upload_to(instance.company, '')
    return parent_path + 'shop_{0}/{1}'.format(instance.name, filename)


class Shop(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(verbose_name="shop photo", blank=True,
                              max_length=255, upload_to=photo_path_shop)
    contact_info = models.ForeignKey(ContactInfo)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Price(models.Model):
    workday_one_hour = models.FloatField(verbose_name="price for an hour (workday)", default=0)
    workday_three_hours = models.FloatField(verbose_name="price for three hours (workday)", default=0)
    work_day = models.FloatField(verbose_name="price for a day (workday)", default=0)
    weekend_one_hour = models.FloatField(verbose_name="price for an hour (weekend)", default=0)
    weekend_three_hours = models.FloatField(verbose_name="price for three hours (weekend)", default=0)
    weekend_day = models.FloatField(verbose_name="price for a day (weekend)", default=0)
    week = models.FloatField(verbose_name="price for a week", default=0)

    def __str__(self):
        return '1h/3h/d/w: {}/{}/{}'.format(
            self.workday_one_hour, self.workday_three_hours, self.work_day, self.week)


def photo_path_bike(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<name>/shop_<name>/bikes/
    parent_path = instance.shop._meta.get_field('photo').upload_to(instance.shop, '')
    return parent_path + 'bikes/{0}'.format(filename)


class Bike(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(verbose_name="bike photo", blank=True,
                              max_length=255, upload_to=photo_path_bike)
    type = models.CharField(max_length=1,
                            choices=(('1', 'male'), ('2', 'female'), ('3', 'kids')),
                            default='1', db_index=True)
    shop = models.ForeignKey(Shop, related_name='bikes', on_delete=models.CASCADE, null=True)
    price = models.ForeignKey(Price, related_name='bikes', db_index=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{} /Shop: {}".format(self.name, self.shop)

    class Meta:
        ordering = ('name',)


class Accessory(models.Model):
    name = models.CharField(max_length=200)
    price = models.ForeignKey(Price, related_name='accessories')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Accessories"


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    bikes = models.ManyToManyField(Bike)
    accessories = models.ManyToManyField(Accessory, blank=True)
    # validation for TimePeriod created in android application
    time_from = models.DateTimeField(verbose_name="from")
    time_to = models.DateTimeField(verbose_name="to")
    # ? make "only visible" Invoice field
    invoice = models.FloatField(default=0)

    def __str__(self):
        return "Order{}, {}".format(self.id, self.client)

    class Meta:
        ordering = ('-id',)
