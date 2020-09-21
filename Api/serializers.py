from rest_framework import serializers  
from blog import models
#from configuration import models



class ArticleRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'titre':obj.titre,
            'description':obj.description,
        }
        
        
class CategorieRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'nom':obj.nom,
            'description':obj.description,
        }
        
        
class TagRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'nom':obj.nom,
            
            
        }

class CommentaireRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'nom':obj.nom,
            'email':obj.email,
            
        }


class TagSerializers(serializers.ModelSerializer):
    Tag_article = ArticleRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Tag  
        fields = '__all__'

class CategorieSerializers(serializers.ModelSerializer):
    categorie_article = ArticleRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Categorie
        fields = '__all__'


class CommentaireSerializers(serializers.ModelSerializer):
    commentaire_article = ArticleRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Commentaire
        fields = '__all__'



class ArticleSerializers(serializers.ModelSerializer):
    categorie = CategorieRelatedField(read_only=True)
    tag = TagRelatedField(read_only=True)
    
    class Meta:
        model = models.Article
        fields = '__all__'
        
class detailSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Article
        fields = '__all__'
        
        