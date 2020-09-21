from rest_framework import serializers  
from configuration import models



class AboutRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'titre':obj.nom,
            'description':obj.description,
        }
        
        
class ContactRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id':obj.id,
            'nom':obj.nom,
            'email':obj.email,
            'message':obj.message,
        }
        
        

class AboutSerializers(serializers.ModelSerializer):
    About = AboutRelatedField(many=True, read_only=True)
    class Meta:
        model = models.About  
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    Contact = ContactRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Contact  
        fields = '__all__'