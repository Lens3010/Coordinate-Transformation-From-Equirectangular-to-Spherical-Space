# Equirectangular Video Projection

Questo progetto implementa una proiezione prospettica di video equirettangolari, consentendo di visualizzare video a 360° in una finestra personalizzabile con angolo di campo (FOV), longitudine (THETA) e latitudine (PHI) regolabili in tempo reale. Utilizza OpenCV per la gestione video e le trasformazioni geometriche.

## Funzionalità

1. **Proiezione Equirettangolare**: Converte il video equirettangolare in una vista prospettica, utilizzando le coordinate di longitudine e latitudine per mappare i pixel correttamente sulla scena 3D.
2. **Interfaccia Interattiva**: Permette all'utente di modificare in tempo reale:
   - **Angolo di Campo (FOV)**: Modificabile tra 1° e 180°.
   - **Longitudine (THETA)** e **Latitudine (PHI)**: Modificabili per cambiare la visualizzazione del video.
3. **Schermo Intero**: Supporta la visualizzazione su finestra a schermo intero con OpenCV, adattando la finestra alla risoluzione del video.
4. **Controlli in Tempo Reale**: È possibile:
   - Aumentare o diminuire l'FOV (tasti 'o' e 'i').
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

# Equirectangular Video Transformation

## Overview

This project provides a Python tool to transform equirectangular (360-degree) video projections into perspective views based on user-defined parameters such as Field of View (FOV), longitude (THETA), and latitude (PHI). It supports real-time video processing and allows for dynamic interaction through keyboard inputs to adjust the view. The tool uses OpenCV for video manipulation and numpy for mathematical operations.

## Features

- **Interactive Perspective Transformation**: Users can adjust the perspective of equirectangular video by modifying the Field of View (FOV), longitude (THETA), and latitude (PHI) through keyboard controls.
- **Real-time Video Processing**: The program continuously processes and displays frames from a video file, applying the necessary transformations.
- **Flexible Video Input**: The tool supports any equirectangular video file, with the ability to handle different resolutions.
- **Transformation Functions**: The code includes functions for converting 3D space coordinates to longitude-latitude (spherical coordinates) and for mapping those coordinates to a 2D perspective projection.

## Installation

1. Clone the repository:
   git clone https://github.com/Lens3010/Coordinate-Transformation-From-Equirectangular-to-Spherical-Space.git

   
