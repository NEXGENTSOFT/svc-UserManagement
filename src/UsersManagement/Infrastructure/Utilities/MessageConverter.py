import json

class MessageConverter:
    @staticmethod
    def text_to_json(text: str) -> dict:
        try:
            json_object = json.loads(text)
            if not isinstance(json_object, dict):
                raise ValueError("Texto plano no es un objeto JSON válido.")
            return json_object
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al convertir texto a JSON: {e}")

    @staticmethod
    def json_to_text(json_object: dict) -> str:
        try:
            text = json.dumps(json_object, ensure_ascii=False)
            return text
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error al convertir JSON a texto: {e}")
