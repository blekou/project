from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact',views.contact)
router.register('about',views.about)


urlpatterns = [
#    path("login/", views.login, name="login"),
]

urlpatterns += router.urls