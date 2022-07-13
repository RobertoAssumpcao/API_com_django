from django.contrib import admin
from mercado.models import Product

class Products(admin.ModelAdmin):
    list_display = ('id','name','quantidade')
    list_display_links = ('name', 'quantidade')
    search_fields = ('name',)

