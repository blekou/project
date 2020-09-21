from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions import Actions



class ContactAdmin(Actions):
    list_display =  ('nom','email','sujet','message','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("Contact",{'fields':['nom','email','sujet','message']}),
        ("standare",{'fields':['status',]})
        ]


class AboutAdmin(Actions):
    list_display =  ('titre','image','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    date_hierarchy = 'date_add'
    list_per_page = 10
    readonly_fields = ['status']
    fieldsets = [
        ("About",{'fields':['titre','description','image']}),
        ("standare",{'fields':['status','date_add', 'date_update', ]})
        ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))

    def detail_logo(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))            


   






def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.About, AboutAdmin)

