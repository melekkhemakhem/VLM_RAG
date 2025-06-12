import base64
import requests
import json

# Charger la liste des frames
with open("frame_files3.json", "r", encoding="utf-8") as f:
    frame_files = json.load(f)

descriptions = {}

for frame_filename in frame_files:
    with open(frame_filename, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    payload = {
        "model": "gemma3:4b",
        "prompt": "maintenant tu as comme un expert en vision par ordinateur, je veux une description détaillée de cette image qui doit contenir(Date et heure(s'il existe) Détails des véhicules uniques et je ne veux pas de réponse rédondante : marque, modèle, couleur et fait des zoom pour capter les détails de matricule(identifier toutes les chiffres et toutes les lettres), Nombre de personnes et leurs détails : position, âge estimé, genre(femme,homme), vêtements, objets portés) et Anomalies éventuelles (objets abandonnés, comportement inhabituel)",
        "images": [image_base64]
    }
    url = "http://127.0.0.1:11534/api/generate"

    try:
        response = requests.post(url, json=payload, stream=True)
        responses = []
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                if 'response' in data:
                    responses.append(data['response'])
        description = ''.join(responses)
    except requests.exceptions.RequestException as e:
        description = f"Erreur lors de la requête : {e}"

    descriptions[frame_filename] = description
    print(f"{frame_filename}: {description}")

with open("descriptions2.json", "w", encoding="utf-8") as f:
    json.dump(descriptions, f, ensure_ascii=False, indent=2)

print("Descriptions enregistrées dans descriptions.json")
