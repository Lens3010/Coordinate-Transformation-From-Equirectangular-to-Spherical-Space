# Equirectangular Video Projection

Questo progetto implementa una proiezione prospettica di video equirettangolari, consentendo di visualizzare video a 360° in una finestra personalizzabile con angolo di campo (FOV), longitudine (THETA) e latitudine (PHI) regolabili in tempo reale. Utilizza OpenCV per la gestione video e le trasformazioni geometriche.

## Funzionalità

1. **Proiezione Equirettangolare**: Converte il video equirettangolare in una vista prospettica, utilizzando le coordinate di longitudine e latitudine per mappare i pixel correttamente sulla scena 3D.
2. **Interfaccia Interattiva**: Permette all'utente di modificare in tempo reale:
   - **Angolo di Campo (FOV)**: Modificabile tra 1° e 180°.
   - **Longitudine (THETA)** e **Latitudine (PHI)**: Modificabili per cambiare la visualizzazione del video.
3. **Schermo Intero**: Supporta la visualizzazione su finestra a schermo intero con OpenCV, adattando la finestra alla risoluzione del video.
4. **Controlli in Tempo Reale**: È possibile:
   - Aumentare o diminuire l'FOV (tasti '+' e '-').
   - Muovere la visualizzazione del video tramite i tasti 'a', 'd', 's', 'w' (movimento orizzontale e verticale).
   - Uscire premendo 'q'.

## Requisiti

- Python 3.x
- OpenCV (cv2)
- NumPy

Puoi installare le dipendenze richieste tramite `pip`:

```bash
pip install opencv-python numpy
```

## Installazione

1. Clona la repository:
   git clone https://github.com/Lens3010/Coordinate-Transformation-From-Equirectangular-to-Spherical-Space.git

# Equirectangular Video Projection

This project implements a perspective projection of equirectangular videos, allowing to display 360° videos in a customizable window with adjustable field of view (FOV), longitude (THETA) and latitude (PHI) in real time. It uses OpenCV for video management and geometric transformations.

## Features

1. **Equirectangular Projection**: Converts equirectangular video into a perspective view, using longitude and latitude coordinates to map pixels correctly on the 3D scene.
2. **Interactive Interface**: Allows the user to modify in real time:
- **Field of View (FOV)**: Changeable between 1° and 180°.
- **Longitude (THETA)** and **Latitude (PHI)**: Changeable to change the video display.
3. **Full Screen**: Supports full screen window display with OpenCV, adapting the window to the video resolution.
4. **Real Time Controls**: You can:
- Increase or decrease the FOV ('+' and '-' keys).
- Move the video display with the 'a', 'd', 's', 'w' keys (horizontal and vertical movement).
- Exit by pressing 'q'.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

You can install the required dependencies via `pip`:

```bash
pip install opencv-python numpy
```
## Installation

1. Clone the repository:
   git clone https://github.com/Lens3010/Coordinate-Transformation-From-Equirectangular-to-Spherical-Space.git

   
