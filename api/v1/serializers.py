from rest_framework import serializers


from .models import Presentation

class PresentationGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ['presentation_id', 'example', 'theme', 'presentation']
        read_only_fields = ['presentation_id', 'presentation']