from django.contrib import admin

# Register your models here.
from firstapp.models import tbladmin,tbluser,tblbookings
admin.site.register(tbladmin)
admin.site.register(tbluser)
admin.site.register(tblbookings)