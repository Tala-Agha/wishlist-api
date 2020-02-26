from django.contrib.auth.models import User
from rest_framework import serializers
from items.models import Item, FavoriteItem

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self,validated_data):
		username = validated_data['username']
		password = validated_data['password']

		new_user = User(username=username, last_name=last_name, first_name=first_name)
		new_user.set_password(password)
		new_user.save()
		return validated_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    added_by = UserSerializer()
    favourited = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['name', 'added_by', 'favourited','detail']
    def get_favourited(self, obj):
        return FavoriteItem.objects.filter(item=obj).count()

class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['name', 'added_by', 'favourited_by']
    def get_favourited_by(self,obj):
        fav_obj = FavoriteItem.objects.filter(item=obj)
        return FavoritedSerializer(fav_obj,many=True).data

class FavoritedSerializer(serializers.ModelSerializer):
    class Meta:
        model= FavoriteItem
        fields = ['user']
