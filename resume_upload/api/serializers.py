from api.models import *
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'dob',  'state',
                  'gender', 'pimage', 'rdoc']
