from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView

from api.serializers import ProfileSerializer
from users.models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileDetailAPIView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        data = {"message": "Hello"}
        return Response(data)
