# Zufallszahlengenerator basierend auf Webcam-Bildern

## Zielsetzung

Entwicklung eines eigenen Zufallszahlengenerators, der auf echtem Zufall basiert. Dabei wird über eine Webcam ein Bild (zum Beispiel einer Plasmakugel oder Lavalampe) aufgenommen und daraus eine Zufallszahl berechnet.

## Projektbeschreibung

In diesem Projekt wird ein Zufallszahlengenerator entwickelt, der reale Bilddaten nutzt, um Zufallszahlen zu generieren. Anhand eines aufgenommenen Bildes wird mithilfe der Bibliotheken `cv2` und `hashlib` ein Hashwert erzeugt, der dann in eine Zufallszahl umgewandelt wird. Das Projekt umfasst die Grundlagen der objektorientierten Programmierung (OOP), den Einsatz von Methoden und Kontrollstrukturen sowie das Testen von Anwendungen.

## Verwendete Bibliotheken und Technologien

- **OpenCV (`cv2`):**  
  Für den Zugriff auf die Webcam und die Bildverarbeitung.

- **Hashlib:**  
  Zum Erzeugen von Hashwerten aus den Bilddaten.

- **Python:**  
  Implementierung des Zufallszahlengenerators unter Verwendung von OOP, Methoden und Kontrollstrukturen.

## Projektdateien

- **`qrng.py`:**  
  Enthält die Implementierung des Zufallszahlengenerators.

- **`test.py`:**  
  Testskript zur Überprüfung der Funktionalität des Zufallszahlengenerators.

- **`camcheck.py`:**  
  Skript zum Testen und Überprüfen der Webcam-Funktionalität.

- **`howto.py`:**  
  Anleitung bzw. Beispielcode zur Verwendung des Zufallszahlengenerators.
