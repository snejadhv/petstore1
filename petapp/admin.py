from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price', 'breed')

# Register your models here.
admin.site.register(Pet, PetAdmin)