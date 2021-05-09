from django.contrib import admin

from home.models import Client
from home.models import Instructor
from home.models import Gruaduated

# Register your models here.

admin.site.register(Client)
admin.site.register(Instructor)
admin.site.register(Gruaduated)