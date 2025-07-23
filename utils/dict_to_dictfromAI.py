import openai
import json
import os
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
        parameters_schema = {
            "type": "object",
            "properties": {
                "items": {
                    "type": "array",
                    "items": extract_schema(schema[0])
                }
            },
            "required": ["items"],
            "additionalProperties": False
        }
    elif isinstance(schema, dict):
        parameters_schema = {
            "type": "object",
            "properties": {
                "items": extract_schema(schema)
            },
            "required": ["items"],
            "additionalProperties": False
        }
    else:
        raise ValueError("schema должен быть list[dict] или dict")

    tools = [{
        "type": "function",
        "function": {
            "name": "regenerate_json",
            "description": "Генерация новой структуры JSON на основе новой темы",
            "parameters": parameters_schema
        }
    }]

    prompt = f"""
    Восстанови JSON такую же по структуре как: {json.dumps(schema, ensure_ascii=False)}.
    Замени текст в полях на тему: "{new_theme}".
    Не превышай длину строк оригинала. Формат строго тот же.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        tools=tools,
        tool_choice={"type": "function", "function": {"name": "regenerate_json"}}
    )

    arguments_str = response.choices[0].message.tool_calls[0].function.arguments
    parsed = json.loads(arguments_str)

    return parsed["items"]

