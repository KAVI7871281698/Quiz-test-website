from django.contrib import admin
from .models import  Question,Option,regiester_page

# Register your models here.
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(regiester_page)

