from django.db import models

# Create your models here.
class tbladmin(models.Model):

    admin_ID = models.CharField(max_length=12, primary_key=True, default='16201519001')
    admin_firstname = models.CharField(max_length=50, default='')
    admin_lastname = models.CharField(max_length=50, default='')
    admin_emailID = models.EmailField(max_length = 254)
    admin_password = models.CharField(max_length=50, default='')
    hall_name = models.CharField(max_length=50, default='')
    hall_address = models.CharField(max_length=250, default='')
    hall_price = models.FloatField()
    hall_capasity = models.IntegerField()
    admin_mobile = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='images/') 


class tbluser(models.Model):
    user_ID = models.CharField(max_length=12, primary_key=True, default='2221519001')
    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    user_email_ID = models.EmailField(max_length = 254)
    user_password = models.CharField(max_length=50, default='')
    user_address = models.CharField(max_length=250, default='')
    user_mobile_number = models.CharField(max_length=10, default='')
    profilepicture = models.ImageField(upload_to='images/')

class tblbookings(models.Model):
    booking_ID = models.CharField(max_length=12, primary_key=True, default='2221519001')
    booking_user_ID = models.ForeignKey("tbluser", on_delete=models.CASCADE)
    booking_admin_ID = models.ForeignKey("tbladmin", on_delete=models.CASCADE)
    booking_total_amount = models.FloatField()
    booking_advance_amount = models.FloatField()
    bookihg_balance_amount = models.FloatField()
    booking_dates = models.DateField()