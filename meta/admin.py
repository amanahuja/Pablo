from django.contrib import admin
from pablo.meta.models import *

class BestsellerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['sentence', 'votes']}),
        ('Date Information',    {'fields': ['save_date'], 
                                    'classes': ['collapse']}),
    ]

admin.site.register(Bestseller, BestsellerAdmin)
