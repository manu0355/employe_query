from django.contrib import admin
from queryapp.models import Company, Language, Programmer

# Register your models here. query
class Companyadmin(admin.ModelAdmin):
    company_list = ['name', 'founder', 'location', 'created_at']

admin.site.register(Company, Companyadmin)
admin.site.register(Language)
admin.site.register(Programmer)