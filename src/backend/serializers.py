from rest_framework import serializers
from backend.models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
		          model = Profile
		          fields = ('id', 'user', 'bio')
