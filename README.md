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
