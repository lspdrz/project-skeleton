from rest_framework import generics

# Models
from backend.models import Profile

# Serializers
from backend.serializers import ProfileSerializer

class ProfileList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Entry objects
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
