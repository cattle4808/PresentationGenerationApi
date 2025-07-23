from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class StatusModel(models.Model):
    class StatusChoices(models.IntegerChoices):
        ERROR = 0, 'Error'
        PROCESSING = 1, 'Processing'
        COMPLETED = 2, 'Completed'

    status = models.IntegerField(default=0, null=False, choices=StatusChoices.choices)

    class Meta:
        abstract = True

class Presentation(BaseModel, StatusModel):
    presentation_id = models.CharField(null=True, blank=True, max_length=100)
    example = models.FileField(upload_to='presentation_examples/')
    theme = models.CharField(max_length=100)
    presentation = models.FileField(upload_to='presentations/', null=True, blank=True)

    def generate_unique_presentation_id(self):
        from uuid import uuid4
        while True:
            new_id = str(uuid4())
            if not Presentation.objects.filter(presentation_id=new_id).exists():
                return new_id

    def save(self, *args, **kwargs):
        if not self.presentation_id:
            self.presentation_id = self.generate_unique_presentation_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.theme


