from django.db import models
from user_api.models import Customer
from user_api.models import Employee

# Create your models here.
class Service(models.Model):
    name = models.CharField("Name", max_length=240)

    class Meta:
        db_table = '"feedback"."service"'

class Feedback(models.Model):
    customer_id = models.ForeignKey(Customer, db_column='customer_id',on_delete=models.SET_NULL, null=True)
    comments = models.TextField()
    service_id = models.ForeignKey(Service,db_column='service_id', on_delete=models.SET_NULL, null=True)
    status = models.CharField("Name", max_length=240, default='Created')
    assigned_to =models.ForeignKey(Employee, db_column='employee_id',on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = '"feedback"."feedback"'

class Action(models.Model):
    Feedback_id = models.ForeignKey(Feedback, db_column='feedback_id', on_delete=models.SET_NULL, null=True)
    employee_id = models.ForeignKey(Employee, db_column='employee_id', on_delete=models.SET_NULL, null=True)
    comments = models.TextField()

    class Meta:
        db_table = '"feedback"."action"'