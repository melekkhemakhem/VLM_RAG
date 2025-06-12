# Projet d'Analyse Vidéo avec Vision par Ordinateur

## Description

Ce projet utilise des modèles de vision par ordinateur (VLM - Vision Language Models) pour analyser automatiquement des vidéos et extraire des informations détaillées sur les véhicules, les personnes et les anomalies présentes dans les images. Le système utilise le modèle Gemma pour générer des descriptions détaillées de chaque frame extraite des vidéos.

## Fonctionnalités

- **Extraction de frames** : Conversion automatique de vidéos MP4 en images individuelles
- **Analyse intelligente** : Utilisation du modèle Gemma 3:4b pour analyser chaque image
- **Détection détaillée** :
  - Identification des véhicules (marque, modèle, couleur, plaques d'immatriculation)
  - Analyse des personnes (âge estimé, genre, vêtements, objets portés)
  - Détection d'anomalies (objets abandonnés, comportements inhabituels)
  - Extraction de dates et heures si disponibles

## Structure du Projet

```
script/
├── build_descriptions_gemma_model.py  # Script principal d'analyse avec Gemma
├── split_video_to_frames.py          # Extraction de frames depuis les vidéos
├── *.mp4                             # Fichiers vidéo source (4.mp4, 5.mp4, 6.mp4, 7.mp4)
├── frames_*/                         # Dossiers contenant les frames extraites
├── frame_files*.json                 # Listes des fichiers de frames
├── descriptions*.json                # Résultats des analyses
└── README.md                         # Ce fichier
```

## Prérequis

### Logiciels requis
- Python 3.7+
- OpenCV (`cv2`)
- Requests
- JSON (inclus dans Python)
- Base64 (inclus dans Python)

### Modèle IA
- Serveur Ollama avec le modèle Gemma 3:4b en cours d'exécution sur `http://127.0.0.1:11534`

## Installation

1. **Cloner le projet** :
```bash
git clone <url-du-repo>
cd script
```

2. **Installer les dépendances Python** :
```bash
pip install opencv-python requests
```

3. **Installer et configurer Ollama** :
```bash
# Installer Ollama (voir https://ollama.ai)
ollama pull gemma3:4b
ollama serve
```

## Utilisation

### 1. Extraction des frames depuis une vidéo

Modifiez le fichier `split_video_to_frames.py` pour spécifier :
- `video_path` : chemin vers votre fichier vidéo
- `output_folder` : dossier de destination des frames
- `frames_per_second` : nombre de frames à extraire par seconde

```bash
python split_video_to_frames.py
```

### 2. Analyse des frames avec Gemma

Assurez-vous que :
- Le serveur Ollama est en cours d'exécution
- Le fichier JSON des frames existe (généré à l'étape 1)

```bash
python build_descriptions_gemma_model.py
```

## Configuration

### Paramètres d'extraction de frames
Dans `split_video_to_frames.py` :
- `frames_per_second = 1` : Extrait 1 frame par seconde
- Modifiez selon vos besoins d'analyse

### Paramètres d'analyse
Dans `build_descriptions_gemma_model.py` :
- URL du serveur Ollama : `http://127.0.0.1:11534/api/generate`
- Modèle utilisé : `gemma3:4b`
- Prompt personnalisable pour l'analyse

## Résultats

Les analyses sont sauvegardées dans des fichiers JSON (`descriptions*.json`) contenant :
- Nom du fichier image analysé
- Description détaillée générée par le modèle
- Informations extraites sur les véhicules, personnes et anomalies

## Exemple de sortie

```json
{
  "frames_3\\frame_0.jpg": "En tant qu'expert en vision par ordinateur, voici une description détaillée de l'image...",
  "frames_3\\frame_1.jpg": "Description de la frame suivante..."
}
```

## Limitations

- La qualité des analyses dépend de la résolution des images
- L'identification des plaques d'immatriculation peut être limitée par l'angle et la netteté
- Les estimations d'âge et de genre sont approximatives
- Nécessite une connexion au serveur Ollama local

## Dépannage

### Erreurs courantes

1. **Erreur de connexion Ollama** :
   - Vérifiez que le serveur Ollama est démarré
   - Confirmez l'URL et le port (11534)

2. **Fichier JSON introuvable** :
   - Exécutez d'abord `split_video_to_frames.py`
   - Vérifiez le nom du fichier JSON dans le script

3. **Erreur OpenCV** :
   - Installez opencv-python : `pip install opencv-python`

## Contribution

Pour contribuer au projet :
1. Fork le repository
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request


