from celery import shared_task


from . import models
from . import serializers

from utils import get_json_structure_from_pptx

@shared_task
def generate_presentation(presentation_id):
    presentation = models.Presentation.objects.get(presentation_id=presentation_id)

    try:
        presentation.status = 1
        presentation.save()

        json_structure = get_json_structure_from_pptx.get_json_structure_from_pptx(presentation.example.path)



    except models.models.ObjectDoesNotExist:
        return

    except Exception as e:
        print(e)
        presentation.status = 0
        presentation.save()
        return


