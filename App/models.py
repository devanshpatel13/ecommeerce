from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator

from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

#
# class Customerregistration(AbstractUser):
#
#     number = models.IntegerField()
#     address = models.CharField(max_length=100)
#     pincode = models.IntegerField()
#
#
#     #
#     # def clean(self):
#     #     super().clean()
#     #     # pass1 = cleanned_data.get("password1")
#     #     # pass2 = cleanned_data.get("password2")
#     #     if not (self.password1 == self.password2):
#     #         raise models.ValidationError("please enter both same passowrd")
#
#
#
# class shopownerreistration(models.Model):
#

CHOICES = (
    ('customer', 'customer'),
    ('shopowner', 'shopowner')
)


class Customer(AbstractUser):
    users = models.CharField(max_length=90, choices=CHOICES)
    # address = models.CharField(max_length=100)
    contact = models.IntegerField(null=True, blank=True)


class Address(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()


class Shopowner(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="image/")
    descripation = models.CharField(max_length=100)
    og_price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    sellprice = models.IntegerField(default=0)
    discountprice = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def dis_price(self):
        return round((((self.og_price) * (self.discount)) / 100))

    def s_price(self):
        return round((((self.og_price) - (self.discountprice))))

    def save(self, *args, **kwargs):
        self.discountprice = self.dis_price()
        self.sellprice = self.s_price()
        super().save(*args, **kwargs)


#
# class Coupon(models.Model):
#     code = models.CharField(max_length=10, unique=True,
#                             validators=[RegexValidator(
#                                 "^[A-Z0-9]*$", "code enter must be uppercase letters & numbers",
#                             )], null=True, blank=True)
#
#     def start_dates(start):
#         sd = timezone.now()
#         if start < sd:
#             raise ValidationError('enter current date..')
#
#     def end_dates(end):
#         ed = timezone.now()
#         if end < ed:
#             raise ValidationError('enter future date....')
#
#     start_date = models.DateTimeField(validators=[start_dates])
#     end_date = models.DateTimeField(validators=[end_dates])
#     discountco = models.IntegerField(default=None, validators=[MaxValueValidator(100)])
#
#
#     def clean(self):
#         super().clean()
#         if not (self.start_date <= self.end_date):
#             raise ValidationError("Don't select Invalid start and end date")
#
#     def save(self, *args, **kwargs):
#         self.code = self.code.upper()
#         return super(Coupon, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.code


class Cart(models.Model):
    # card_id = models.UUIDField(default=uuid.uuid4())
    cart_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    # active = models.BooleanField(default=False)
    #
    # @property
    # def product_total(self):
    #     return ((self.product.sellprice)*(self.quantity))
    #
    # @property
    # def Or_price(self):
    #     return ((self.product.og_price)*(self.quantity))
    #
    # @property
    # def total_save(self):
    #     return ((self.product.discountprice)*(self.quantity))
    #
    # def __str__(self):
    #     return str(self.product.name)


class cart_item(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Shopowner, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def product_total(self):
        return ((self.product.sellprice) * (self.quantity))

    @property
    def Or_price(self):
        return ((self.product.og_price) * (self.quantity))

    @property
    def total_save(self):
        return ((self.product.discountprice) * (self.quantity))

    def __str__(self):
        return str(self.product.name)


st = (
    ('Order received', 'Order received'),
    ('Shipped', 'Shipped'),
    ('out for delivery', 'out for delivery'),
    ('Delivered', 'Delivered')
)


class Myorder(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Shopowner, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=100, choices=st, default="Pending")

    def __str__(self):
        return self.user.username

    @property
    def product_total(self):
        return ((self.product.sellprice) * (self.quantity))

    @property
    def Or_price(self):
        return ((self.product.og_price) * (self.quantity))

    @property
    def total_save(self):
        return ((self.product.discountprice) * (self.quantity))


class Couponcode(models.Model):
    code = models.CharField(max_length=10)
    # course =models.ForeignKey(Shopowner,on_delete=models.CASCADE, related_name="coupons")
    discount = models.IntegerField(default=0)
