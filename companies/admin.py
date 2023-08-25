from django.contrib import admin
from companies.models import District, Company, CompanyNet, Category, Good

admin.site.register(District)
admin.site.register(CompanyNet)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Good)

