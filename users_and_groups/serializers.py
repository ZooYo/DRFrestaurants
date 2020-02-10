from django.contrib.auth.models import User, Group
from rest_framework import serializers
from users_and_groups.models import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    birth_date = serializers.DateField(source='profile.birth_date')
    phone_number = serializers.CharField(max_length=15, source='profile.phone_number')

    def create(self, validated_data):
        print(validated_data)
        validated_data.pop('profile')
        print(validated_data)
        # validated_data['profile'] = Profile.objects.create(**profile)
        user = User.objects.create(**validated_data)


        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', "password", "birth_date", "phone_number"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

