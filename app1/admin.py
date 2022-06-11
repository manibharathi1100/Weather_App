from django.contrib import admin
from .models import RegisterModel

# Register your models here.


class RegisterModelAdmin(admin.ModelAdmin):
    #list_display = ['firstname', 'lastname', 'age', 'dob', 'gender', 'email', 'phone', 'username', 'password']
    pass

admin.site.register(RegisterModel, RegisterModelAdmin)
