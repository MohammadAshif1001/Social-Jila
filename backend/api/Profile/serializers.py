from rest_framework import serializers
from Profile.models import UserProfile
class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['password']