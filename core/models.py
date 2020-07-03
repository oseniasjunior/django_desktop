from django.db import models
from datetime import datetime


# Create your models here.
class Person(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=100
    )
    gender = models.CharField(
        db_column='cs_gender',
        null=False,
        max_length=1
    )
    salary = models.DecimalField(
        db_column='nb_salary',
        null=False,
        max_digits=10,
        decimal_places=2
    )
    date_birth = models.DateField(
        db_column='dt_birth',
        null=False
    )

    class Meta:
        db_table = 'person'
        managed = True

    @property
    def age(self):
        _now = datetime.now().date()
        diff = _now - self.date_birth
        return int(diff.days / 365)
