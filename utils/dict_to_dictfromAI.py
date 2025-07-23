import openai
import json
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

client = openai.OpenAI()


def renew_json(schema: list[dict] | dict, new_theme: str) -> list[dict] | dict:
    def extract_schema(example: dict) -> dict:
        props = {}
        for key, value in example.items():
            props[key] = {
                "type": "string",
                "maxLength": len(value) if isinstance(value, str) else 200
            }
        return {
            "type": "object",
            "properties": props,
            "required": list(props.keys()),
            "additionalProperties": False
        }

    if isinstance(schema, list):
        schema_schema = {
            "type": "array",
            "items": extract_schema(schema[0])
        }
    elif isinstance(schema, dict):
        schema_schema = extract_schema(schema)
    else:
        raise ValueError("schema должен быть list[dict] или dict")

    functions = [{
        "name": "regenerate_json",
        "description": "Генерация новой структуры JSON на основе новой темы",
        "parameters": schema_schema
    }]

    prompt = f"""
    Восстанови JSON такую же по структуре как: {json.dumps(schema, ensure_ascii=False)}.
    Только замени содержимое всех строк на тему: "{new_theme}".
    Сохрани длину каждого поля не длиннее оригинала.
    Ответ должен строго соответствовать структуре.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        tools=functions,
        tool_choice={"type": "function", "function": {"name": "regenerate_json"}},
    )

    arguments_str = response.choices[0].message.tool_calls[0].function.arguments
    parsed = json.loads(arguments_str)

    return parsed
