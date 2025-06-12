import cv2
import os
import json

video_path = "7.mp4"
output_folder = "frames_3"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frames_per_second = 1

frame_count = 0
frame_id = 0
frame_files = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % int(fps / frames_per_second) == 0:
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_files.append(frame_filename)
        frame_count += 1

    frame_id += 1

cap.release()
print(f"{frame_count} frames extraites.")

# Sauvegarder la liste des frames dans un fichier JSON
with open("frame_files3.json", "w", encoding="utf-8") as f:
    json.dump(frame_files, f, ensure_ascii=False, indent=2)