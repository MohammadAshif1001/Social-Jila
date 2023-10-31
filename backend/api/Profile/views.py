from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from Profile.models import UserProfile
from Profile.serializers import ProfileDetailSerializer

class ProfileDetails(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    
    queryset=UserProfile.objects.all()
    serializer_class=ProfileDetailSerializer
    lookup_field='pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

