from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorie',views.categorie_list)
router.register('article',views.article)
router.register('detail',views.categorie_detail)
router.register('tag',views.tag)
router.register('commentaire',views.commentaire)

urlpatterns = [
#    path("login/", views.login, name="login"),
]

urlpatterns += router.urls