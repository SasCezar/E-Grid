from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField


class Address(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    # TODO Add GeoSpatial
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class AdministrativeOrganization(Subject):
    responsible = models.CharField(max_length=30)
    org_type = models.CharField(max_length=30)


class Product(models.Model):
    specification = models.TextField()
    description = models.CharField(max_length=1024)


class Order(models.Model):
    buyer_id = models.ForeignKey(AdministrativeOrganization, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


PRODUCER_TYPES = (('Maker', 'Independent Maker'),
                  ('Factory', 'Industrial Factory'),
                  ('Other', 'Other type of Producer'))


class Producer(Subject):
    producer_type = MultiSelectField(choices=PRODUCER_TYPES)
    category = models.CharField(max_length=30)


class FinishedProduct(models.Model):
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    donation = models.BinaryField(default=False)


class GatheringCenter(Subject):
    administrated_by = models.ForeignKey(AdministrativeOrganization, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=30)


class Dispatch(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    finished_product_id = models.ForeignKey(FinishedProduct, on_delete=models.CASCADE)
    gathering_center_id = models.ForeignKey(GatheringCenter, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("order_id", "finished_product_id", "gathering_center_id"))


HEALTH_CENTER_TYPES = (('Hospital', 'Hospital'),
                       ('Pharmacy', 'Pharmacy'),
                       ('Medic', 'Family Practitioner'),
                       ('Other', 'Other type of center'))


class HealthCenter(Subject):
    manager = models.CharField(max_length=30)
    center_type = MultiSelectField(choices=HEALTH_CENTER_TYPES)


class Asks(models.Model):
    product_id = models.ForeignKey(Producer, on_delete=models.CASCADE)
    center_id = models.ForeignKey(HealthCenter, on_delete=models.CASCADE)
    administrator_id = models.ForeignKey(AdministrativeOrganization, on_delete=models.CASCADE)
