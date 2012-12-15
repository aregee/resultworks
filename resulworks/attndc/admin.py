from result.models import *
from attndc.models import *
from django.contrib import admin


#class studp(admin.ModelAdmin):
#   list_display = ('stud')

class atdsp(admin.ModelAdmin):
    list_display = ('status','date')

#admin.site.register(Attnd,studp)
admin.site.register(choice,atdsp)
