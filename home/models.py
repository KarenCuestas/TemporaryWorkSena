from django.db import models
from django.db.models.fields import CharField

ENUM_OPTIONS = ('si', 'no')

# Create your models here.
class Client(models.Model) :
    id_client = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    sex = models.CharField(max_length=10)
    document_type = models.CharField(max_length=5)
    number_document = models.IntegerField(12)
    phone = models.CharField(max_length=12)
    email_adrres = models.CharField(max_length=30)
    addres = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    user_client = models.CharField(max_length=20)
    password_client = models.CharField(max_length=20)


class Instructor(models.Model) :
    id_instructor = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    document_type = models.CharField(max_length=5)
    number_document = models.IntegerField(12)
    email_adrres = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    user_instructor = models.CharField(max_length=20)
    password_instructor = models.CharField(max_length=20)


class Gruaduated(models.Model) :
    id_graduated = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    document_type = models.CharField(max_length=5)
    number_document = models.IntegerField(12)
    email_adrres = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    addres = models.CharField(max_length=30)
    addres_enterprise = models.CharField(max_length=100)
    name_enterprise = models.CharField(max_length=100)
    position = models.CharField(max_length=4)
    experencie = CharField(max_length=4)
    academic_training = models.CharField(max_length=25)
    program_name = models.CharField(max_length=25)
    user_graduated = models.CharField(max_length=20)
    password_graduated = models.CharField(max_length=20)
    id_instructor = models.IntegerField(default=0)

class Reviews(models.Model):
    id_review = models.AutoField(primary_key=True, auto_created=True)
    menssage = models.CharField(max_length=100)
    graduado = models.ForeignKey(Gruaduated, on_delete=models.CASCADE)
    #se encuentra como graduado_id
    id_instructor = models.IntegerField(default=0)