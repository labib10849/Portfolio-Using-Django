from django.contrib import admin
from Base.models import Contact 
# Register your models here.
admin.site.register(Contact)






admin.site.site_header = 'Portfolio | Admin Panel'
admin.site.site_title = 'Portfolio | Portfolio Website'
admin.site.index_title= 'Portfolio Administration'
