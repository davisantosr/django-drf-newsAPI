from rest_framework import serializers

from datetime import datetime
from django.utils import timesince

from news.models import Article



class ArticleSerializer(serializers.ModelSerializer):

  time_since_publication = serializers.SerializerMethodField()

  class Meta:
    model = Article
    fields = ("__all__")
    #exclude =  ("id", )
    #fields = ("id", title, description, )
    
  def get_time_since_publication(self, object):
    publication_date = object.publication_date
    now = datetime.now()
    time_delta = timesince(publication_date, now)
    return time_delta

# =====================================================


# class ArticleSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   author = serializers.CharField()
#   title = serializers.CharField()
#   description = serializers.CharField()
#   body = serializers.CharField()
#   location = serializers.CharField()
#   publication_date = serializers.DateField()
#   active = serializers.BooleanField()
#   created_at = serializers.DateTimeField(read_only=True)
#   updated_at = serializers.DateTimeField(read_only=True)


#   def create(self, validated_data):
#     print(validated_data)
#     return Article.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.author = validated_data.get('author', instance.author)
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description', instance.author)
#     instance.body = validated_data.get('body', instance.body)
#     instance.location = validated_data.get('location', instance.location)
#     instance.publication_date = validated_data.get('date', instance.publication_date)
#     instance.active = validated_data.get('active', instance.active)

#     instance.save()
    
#   #OBJECT LEVEL VALIDATION
#   def validate(self, data):
#     """ Check if title anda description are different """
#     if data["title"] == data["description"]:
#       raise serializers.ValidationError("Title and Description must be different")

#     return data

#   #FIELD LEVEL VALIDATION
#   def validate_title(self, value):
#     if len(value) < 60:
#       raise serializers.ValidationError("Title must have at least 60 chars long.")
#     return value

