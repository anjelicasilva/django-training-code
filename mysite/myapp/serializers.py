from rest_framework import serializers
from.models import Role, User, EasterEgg

class RoleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Role
       fields = (['name'])

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = (['firstname','lastname', 'email', 'password'])


class EasterEggSerializer(serializers.ModelSerializer):
   class Meta:
       model = EasterEgg
       fields = (['name'])
