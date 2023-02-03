from django.db import models

class Customer(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = '"feedback"."customer"'

class Employee(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"feedback"."employee"'



