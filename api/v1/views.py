from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models
from .tasks import generate_presentation

class GeneratePresentation(generics.ListCreateAPIView):
    queryset = models.Presentation.objects.all()
    serializer_class = serializers.PresentationGenerationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        presentation = serializer.save()

        generate_presentation.delay(presentation.presentation_id)

        return Response(
            {
                "message": "Генерация запущена",
                "presentation_id": presentation.presentation_id
            },
            status=status.HTTP_201_CREATED
        )





