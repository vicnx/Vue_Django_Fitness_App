from rest_framework import serializers
from app.modules.profiles.serializers import ProfileSerializer
from app.modules.fitness.category.serializers import CategorySerializer

from .models import Exercice

class ExerciceSerializer(serializers.HyperlinkedModelSerializer):
    # fullname = serializers.SerializerMethodField()
    # concatenar = serializers.SerializerMethodField('asdf')

    # def asdf(self,obj):
    #     return obj.name+"STRING"
    
    # def get_fullname(self,obj):
    #     return obj.name+"FULLNAME"

    author = ProfileSerializer(read_only=True)
    # categories = CategorySerializer()
    description = serializers.CharField(required=False)

    class Meta:
        model = Exercice
        fields = ('id', 'slug', 'name', 'description', 'image', 'author')
        # fields = ('id', 'slug', 'name', 'description', 'image', 'author', 'categories')

    
    def create(self, validated_data):
        author = self.context.get('author', None)
        exercice = Exercice.objects.create(author=author, **validated_data)
        return exercice




# class ArticleSerializer(serializers.ModelSerializer):
#     author = ProfileSerializer(read_only=True)
#     description = serializers.CharField(required=False)
#     slug = serializers.SlugField(required=False)

#     favorited = serializers.SerializerMethodField()
#     favoritesCount = serializers.SerializerMethodField(
#         method_name='get_favorites_count'
#     )

#     tagList = TagRelatedField(many=True, required=False, source='tags')

#     # Django REST Framework makes it possible to create a read-only field that
#     # gets it's value by calling a function. In this case, the client expects
#     # `created_at` to be called `createdAt` and `updated_at` to be `updatedAt`.
#     # `serializers.SerializerMethodField` is a good way to avoid having the
#     # requirements of the client leak into our API.
#     createdAt = serializers.SerializerMethodField(method_name='get_created_at')
#     updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

#     class Meta:
#         model = Article
#         fields = (
#             'author',
#             'body',
#             'createdAt',
#             'description',
#             'favorited',
#             'favoritesCount',
#             'slug',
#             'tagList',
#             'title',
#             'updatedAt',
#         )

#     def create(self, validated_data):
#         author = self.context.get('author', None)

#         tags = validated_data.pop('tags', [])

#         article = Article.objects.create(author=author, **validated_data)

#         for tag in tags:
#             article.tags.add(tag)

#         return article

#     def get_created_at(self, instance):
#         return instance.created_at.isoformat()

#     def get_favorited(self, instance):
#         request = self.context.get('request', None)

#         if request is None:
#             return False

#         # if not request.user.is_authenticated():
#         if not request.user.is_authenticated:
#             return False

#         return request.user.profile.has_favorited(instance)

#     def get_favorites_count(self, instance):
#         return instance.favorited_by.count()

#     def get_updated_at(self, instance):
#         return instance.updated_at.isoformat()