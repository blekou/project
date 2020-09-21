from django.db import models

class Contact(models.Model):
    

    nom = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    sujet = models.CharField(max_length=50,null=True)
    message = models.TextField(null=True)
    

    
    date_add = models.DateTimeField(auto_now=True,null=True)
    date_update = models.DateTimeField(auto_now_add=True,null=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.nom


class About(models.Model):
    

    titre = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='image/about', null=True)
    description = models.TextField(null=True)
    

    
    date_add = models.DateTimeField(null=True)
    date_update = models.DateTimeField(null=True)
    status = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.titre