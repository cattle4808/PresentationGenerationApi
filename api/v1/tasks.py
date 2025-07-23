from celery import shared_task

from . import models
from . import serializers

from utils import renew_pptx

@shared_task
def generate_presentation(presentation_id):
    presentation = models.Presentation.objects.get(presentation_id=presentation_id)

    try:
        presentation.status = 1
        presentation.save()

        new_pptx = renew_pptx(presentation.example.path, presentation.theme)

        presentation.presentation = new_pptx
        presentation.status = 2
        presentation.save()

        print("generated")
        return "generated"


    except models.models.ObjectDoesNotExist as e:
        print(e)

    except Exception as e:
        print(e)
        presentation.status = 0
        presentation.save()
        return


