from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions import Actions


class CommentaireInline(admin.StackedInline):
    model = models.Commentaire
    extra = 1


class ArticleAdmin(Actions):
    fieldsets = [
        ("infocategory",{'fields':['titre','image','description','categorie','contenu','tag']}),
        ("standare",{'fields':['status',]})
        ]
    list_display =  ('titre','date_add', 'date_update', 'status','categorie','image_view')
    list_filter =  ('status',)
    search_fields = ('titre','categorie',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre',]
    ordering = ['titre',]
    filter_horizontal = ('tag',)
    list_per_page = 10
    readonly_fields = ['detail_image']
    # inlines = [
    #     CommentaireInline
    #     ]

    def image_view(self,obj):
        return mark_safe("<img src = '{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}/" width ="100px" height ="50px">'.format(url = obj.image.url))

# class ArticleInline(admin.TabularInline):
#     model = models.Article
#     extra = 1

class CategorieAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    readonly_fields = ['detail_image']
    # inlines = [
    #     ArticleInline,
    # ]
    fieldsets = [
        ("infocategory",{'fields':['nom','image','description']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))

    def detail_image(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))        

# class CategorieInline(admin.TabularInline):
#     model = models.Article
#     extra = 1


class TagAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom',]}),
        ("standare",{'fields':['status',]})
        ]


class CommentaireAdmin(Actions):
    list_display =  ('nom', 'article', 'date_add', 'date_update', 'status',)
    list_filter =  ('status', 'article')
    search_fields = ('article', 'slug',)
    date_hierarchy = 'date_add'
    list_display_links = ['article',]
    ordering = ['article',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','article','commentaire']}),
        ("standare",{'fields':['status',]})
        ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)