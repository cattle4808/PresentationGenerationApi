from rest_framework import views, generics


from . import serializers
from . import models


class GeneratePresentation(generics.ListCreateAPIView):
    queryset = models.Presentation.objects.all()
    serializer_class = serializers.PresentationGenerationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        presentation = serializer.save()

        presentation_id = presentation.presentation_id




