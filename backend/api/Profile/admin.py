from django.contrib import admin
from Profile.models import UserProfile,Follower

admin.site.register([UserProfile,Follower])
admin.site.site_header='Syncraze'
admin.site.site_title='Syncraze'
