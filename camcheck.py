import cv2

def find_available_cameras():
  available_cameras = []
  for camera_id in range(10):
    cap = cv2.VideoCapture(camera_id)
    if cap.isOpened():
      print(f"Kamera mit ID {camera_id} ist verfügbar.")
      available_cameras.append(camera_id)
      cap.release()
    else:
      print(f"Kamera mit ID {camera_id} nicht verfügbar.")

  return available_cameras

available_cameras = find_available_cameras()
print("Verfügbare Kamera-IDs:", available_cameras)
