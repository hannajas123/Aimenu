from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=20)
class Menu(models.Model):
    item_name=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    price=models.CharField(max_length=50)
    neutral=models.IntegerField(default=0)
    positive=models.IntegerField(default=0)
    negative=models.IntegerField(default=0)
class Special_Menu(models.Model):
    MENU = models.ForeignKey(Menu, on_delete=models.CASCADE,default="")
class Customer(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)

class Staff(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    type = models.CharField(max_length=50)


class Order_main(models.Model):
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default="")
    date=models.DateField(max_length=20)
    amount=models.CharField(max_length=30)
    status=models.CharField(max_length=30,default="")
class Order_sub(models.Model):
    MENU=models.ForeignKey(Menu,on_delete=models.CASCADE,default="")
    ORDERMAIN=models.ForeignKey(Order_main,on_delete=models.CASCADE,default="")
    quantity=models.CharField(max_length=30)
class Order_delay(models.Model):
    ORDERMAIN=models.ForeignKey(Order_main,on_delete=models.CASCADE,default="")
    Time_in_minutes=models.TimeField(max_length=20)
class Cart(models.Model):
    MENU=models.ForeignKey(Menu,on_delete=models.CASCADE,default="")
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default="")
    quantity=models.CharField(max_length=30)
class Allocation(models.Model):
    STAFF=models.ForeignKey(Staff,on_delete=models.CASCADE,default="")
    ORDERMAIN=models.ForeignKey(Order_main,on_delete=models.CASCADE,default="")
    status=models.CharField(max_length=30)
    date=models.DateField(max_length=30)
    time=models.CharField(max_length=30,default="")
class Table(models.Model):
    table_no=models.CharField(max_length=30)
    no_of_seats=models.CharField(max_length=30)
class Payment(models.Model):
    ORDERMAIN = models.ForeignKey(Order_main, on_delete=models.CASCADE,default="")
    acc_no = models.CharField(max_length=40)
    date = models.DateField(max_length=30)
class Reviews(models.Model):
    MENU=models.ForeignKey(Menu,on_delete=models.CASCADE,default="")
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default="")
    date=models.DateField(max_length=20)
    time=models.TimeField(max_length=20)
    review=models.CharField(max_length=3000,default="")
    rating=models.CharField(max_length=30)
class Complaint(models.Model):
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE,default="")
    date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    complaints=models.CharField(max_length=300)
    reply=models.CharField(max_length=300)
    status=models.CharField(max_length=50)

class Bank(models.Model):
    accno = models.CharField(max_length=100)
    cardno = models.BigIntegerField()
    cardholder = models.CharField(max_length=100)
    Cvv = models.IntegerField()
    expirydate = models.CharField(max_length=100)
    Balance = models.FloatField()