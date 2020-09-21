from django.db import models

class Categorie(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)

    date_add = models.DateTimeField(null=True)
    date_update = models.DateTimeField(null=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.nom


class Tag(models.Model):
    
    nom = models.CharField(max_length=50)
    
    date_add = models.DateTimeField(null=True)
    date_update = models.DateTimeField(null=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'

    def __str__(self):
        return self.nom





class Article(models.Model):
    
    titre = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)
    contenu = models.TextField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name="categorie_article")
    tag = models.ManyToManyField(Tag,related_name="tag_article")

    date_add = models.DateTimeField(null=True)
    date_update = models.DateTimeField(null=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    

    nom = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    message = models.CharField(max_length=50,null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name="article_commentaire")

    
    date_add = models.DateTimeField(null=True)
    date_update = models.DateTimeField(null=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaire'

    def __str__(self):
        return self.nom