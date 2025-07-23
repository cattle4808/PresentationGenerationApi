from get_json_structure_from_pptx import extract_detailed_structure
from dict_to_dictfromAI import renew_json
from to_pptx_from_json_new_sctructure import replace_text_with_json_structure


def renew_pptx(pptx_path: str, new_theme: str):
    json_structure = extract_detailed_structure(pptx_path)
    renew_json(json_structure, new_theme)
    new_pptx = replace_text_with_json_structure(pptx_path, json_structure)
    print(new_pptx)
    return new_pptx

def save_pptx(pptx_path: str, new_pptx):
    new_pptx.save(pptx_path)

__all__ = [
    'save_pptx',
    'renew_pptx'
]