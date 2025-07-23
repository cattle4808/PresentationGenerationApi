import openai

from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def renew_json(schema: list | dict, new_theme: str) -> list[dict] | dict:
    ...
