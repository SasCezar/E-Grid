from django.db import models

# Create your models here.


class Address(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=5, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=5, null=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'


class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    org_type = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1024)
    specification = models.TextField()
    image_url = models.CharField(max_length=512, null=True)
    file_url = models.CharField(max_length=512, null=True)


class Order(models.Model):
    buyer_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class FinishedProduct(models.Model):
    producer_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    donation = models.BinaryField(default=False)


class GatheringCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    administrated_by = models.ForeignKey(Organization, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=30)


class Dispatch(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    finished_product_id = models.ForeignKey(FinishedProduct, on_delete=models.CASCADE)
    gathering_center_id = models.ForeignKey(GatheringCenter, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("order_id", "finished_product_id", "gathering_center_id"))
