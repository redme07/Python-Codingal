import json
import requests
import os

def handler(request):
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

    body = request.json()
    image_data = body.get("image")

    if not image_data:
        return {
            "statusCode": 400,
            "body": json.dumps({"result": "No image received"})
        }

    image_base64 = image_data.split(",")[1]

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{
            "parts": [
                {"text": "Analyze this plant leaf and tell me if it has any nutrient deficiency."},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": image_base64
                    }
                }
            ]
        }]
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        text = result["candidates"][0]["content"]["parts"][0]["text"]

        return {
            "statusCode": 200,
            "body": json.dumps({"result": text})
        }

    return {
        "statusCode": 500,
        "body": json.dumps({"result": "Gemini API error"})
    }