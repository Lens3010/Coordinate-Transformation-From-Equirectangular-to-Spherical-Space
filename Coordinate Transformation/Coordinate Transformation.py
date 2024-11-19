import os
import cv2
import numpy as np

def xyz2lonlat(xyz):
    #aliasing, cioè assegniamo un altro nome a una funzione o variabile per abbreviare il codice.
    atan2 = np.arctan2
    asin = np.arcsin
    #Questa riga calcola la norma di ciascun vettore nella matrice xyz. 
    # axis= -1 specifica che la norma deve essere calcolata lungo l'ultimo asse della matrice
    #keepdims mantiene le dimensioni della matrice risultante in modo che possa essere trasmessa 
    #correttamente durante le operazioni successive.
    norm = np.linalg.norm(xyz, axis=-1, keepdims=True)
    #Qui viene normalizzata la matrice xyz dividendo ciascun vettore per la sua norma
    #Questo passaggio che tutti i vettori abbiano lunnghezza unitaria
    xyz_norm = xyz / norm
    #Queste righe estraggono le componenti x, y e z dei vettori normalizzati xyz_norm e le assegnano alle variabili x, y e z rispettivamente. 
    #L'uso di ... indica che stiamo selezionando tutte le righe e una sola colonna corrispondente alla componente specificata.
    x = xyz_norm[..., 0:1]
    y = xyz_norm[..., 1:2]
    z = xyz_norm[..., 2:]
    #Qui viene calcolata la longitudine utilizzando la funzione atan2, che 
    #calcola l'arcotangente di y/x. In questo caso, x rappresenta la componente x del vettore e z rappresenta la componente z. 
    #Questo calcolo è tipico quando si convertono coordinate cartesiane in coordinate sferiche.
    lon = atan2(x, z)
    #Qui viene calcolata la latitudine utilizzando la funzione asin, che calcola l'arcoseno di un valore. In questo caso, y 
    #rappresenta la componente y del vettore. 
    #Questo calcolo è anche tipico nella conversione di coordinate cartesiane in coordinate sferiche.
    lat = asin(y)
    #Qui vengono creati una lista lst che contiene la longitudine e la latitudine calcolate.
    lst = [lon, lat]
    #viene concatenata la lista lst lungo l'asse -1 (cioè l'asse dell'ultima dimensione) per creare la matrice di output out, 
    #che contiene le coordinate sferiche longitudine-latitudine.
    out = np.concatenate(lst, axis=-1)
    #Ritorna la matrice delle coordinate sferiche
    return out

def lonlat2XY(lonlat, shape):
 #In questa riga, la coordinata X viene calcolata. lonlat[..., 0:1] estrae la prima colonna della matrice lonlat, 
 #che rappresenta la longitudine. Il valore della longitudine viene diviso per 2 * np.pi, che normalizza la longitudine in 
 #un intervallo tra -0.5 e 0.5. Aggiungendo 0.5, l'intervallo diventa compreso tra 0 e 1. Infine, moltiplicando per (shape[1] - 1), 
 #questa scala viene adattata alla larghezza dell'immagine meno 1.
    X = (lonlat[..., 0:1] / (2 * np.pi) + 0.5) * (shape[1] - 1)
    Y = (lonlat[..., 1:] / (np.pi) + 0.5) * (shape[0] - 1) 
    #In questa riga, la coordinata Y viene calcolata. lonlat[..., 1:] estrae la 
    #seconda colonna della matrice lonlat, che rappresenta la latitudine. Il valore della latitudine viene diviso per np.pi, 
    #normalizzando la latitudine in un intervallo tra -0.5 e 0.5. Aggiungendo 0.5, l'intervallo diventa compreso tra 0 e 1. 
    #Infine, moltiplicando per (shape[0] - 1), questa scala viene adattata all'altezza dell'immagine meno 1.
    Y = (lonlat[..., 1:] / (np.pi) + 0.5) * (shape[0] - 1)
    #Viene creato un elenco contenente le coordinate X e Y calcolate.
    lst = [X, Y]
    #Le coordinate X e Y vengono concatenate lungo l'asse -1 (cioè l'asse dell'ultima dimensione), 
    #quindi otteniamo una matrice di coordinate con le coordinate X e Y accoppiate.
    out = np.concatenate(lst, axis=-1)
    #Restituisce la matrice delle coordinate.
    return out 

class Equirectangular:
    def __init__(self, video_name):
        self._cap = cv2.VideoCapture(video_name)
        self._height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self._width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    def GetPerspective(self, FOV, THETA, PHI, width, height):
         #Qui viene calcolata la lunghezza focale (f) in base all'angolo di campo visivo (FOV), all'altezza (height) e 
         #alla larghezza (width) dell'immagine proiettata. Viene utilizzata la formula della proiezione prospettica per 
         #calcolare la lunghezza focale.
        f = 0.5 * width * 1 / np.tan(0.5 * FOV / 180.0 * np.pi)
        #Queste righe calcolano le coordinate del punto principale, che è il punto in cui 
        #l'asse ottico della telecamera interseca il piano dell'immagine. Questo punto è al centro dell'immagine.
        cx = (width - 1) / 2.0
        cy = (height - 1) / 2.0
        #Qui viene creata la matrice di calibrazione (K), che è una matrice 3x3 che contiene i parametri intrinseci
        #della fotocamera, come la lunghezza focale e le coordinate del punto principale.
        K = np.array([
                [f, 0, cx],
                [0, f, cy],
                [0, 0,  1],
            ], np.float32)
        # Viene calcolata l'inversa della matrice di calibrazione.
        K_inv = np.linalg.inv(K)
       #Viene letto un frame dal video utilizzando il metodo read dell'oggetto VideoCapture. 
       #La variabile ret indica se il frame è stato letto correttamente o meno, mentre frame contiene il frame stesso.
        ret, frame = self._cap.read()
        if not ret:
            return None
        #Vengono generate griglie di coordinate x e y corrispondenti alla larghezza e all'altezza dell'immagine proiettata.
        x = np.arange(width)
        y = np.arange(height)
        #Vengono create meshgrid (griglie) a partire dalle coordinate x e y. Questo è utile per la rappresentazione dei punti nell'immagine.
        x, y = np.meshgrid(x, y)
        #Viene creata una matrice z composta da uno, poiché in 
        #un'immagine prospettica tutti i punti si trovano a una distanza unitaria dal piano dell'immagine.
        z = np.ones_like(x)
        #Vengono concatenate le matrici x, y e z lungo 
        #l'asse -1 per creare una matrice xyz che rappresenta le coordinate spaziali dei punti nell'immagine.
        xyz = np.concatenate([x[..., None], y[..., None], z[..., None]], axis=-1)
        # Vengono trasformate le coordinate spaziali dei punti nell'immagine utilizzando 
        #l'inversa della matrice di calibrazione. Questo passaggio è necessario per 
        #ottenere le coordinate 3D dei punti rispetto alla fotocamera.
        xyz = xyz @ K_inv.T
       # Viene creato un vettore y_axis che rappresenta l'asse y nel sistema di coordinate tridimensionale
        y_axis = np.array([0.0, 1.0, 0.0], np.float32)
         #Viene creato un vettore x_axis che rappresenta l'asse x nel sistema di coordinate tridimensionale.
        x_axis = np.array([1.0, 0.0, 0.0], np.float32)
         #Viene utilizzata la funzione cv2.Rodrigues per convertire 
        #l'asse y_axis in una matrice di rotazione R1 che ruota di un angolo specificato da THETA (in radianti) 
        #intorno all'asse y.
        R1, _ = cv2.Rodrigues(y_axis * np.radians(THETA))
       #Viene utilizzata la funzione cv2.Rodrigues per convertire la combinazione 
        #dell'asse x_axis ruotato da R1 in una matrice di rotazione R2 che ruota di 
        #un angolo specificato da PHI (in radianti) intorno all'asse x.
        R2, _ = cv2.Rodrigues(np.dot(R1, x_axis) * np.radians(PHI))
         #Viene calcolata la matrice di rotazione composta moltiplicando le
        #matrici di rotazione R1 e R2. Questa operazione è necessaria per combinare le rotazioni intorno agli assi x e y.
        R = R2 @ R1
        #Vengono applicate le rotazioni alla matrice xyz dei punti nello spazio moltiplicando xyz 
        #per la trasposta della matrice di rotazione R. Questo trasforma le coordinate dei punti nel sistema di coordinate del video.
        xyz = xyz @ R.T
        # Viene chiamata la funzione xyz2lonlat per convertire le coordinate tridimensionali dei punti in coordinate longitudine-latitudine.
        lonlat = xyz2lonlat(xyz)
    #Viene chiamata la funzione lonlat2XY per convertire le coordinate longitudine-latitudine in 
    #coordinate bidimensionali dell'immagine prospettica. Questo calcola le coordinate X e Y dei punti nell'immagine prospettica.
        XY = lonlat2XY(lonlat, shape=(self._height, self._width)).astype(np.float32)
   # Viene utilizzata la funzione cv2.remap per applicare la trasformazione prospettica all'immagine frame utilizzando le coordinate X e Y 
    #calcolate. Viene utilizzato l'interpolatore cv2.INTER_CUBIC per ottenere una buona qualità dell'immagine risultante. 
    #Il parametro borderMode=cv2.BORDER_WRAP gestisce i pixel al di fuori dell'immagine prospettica.
        persp = cv2.remap(frame, XY[..., 0], XY[..., 1], cv2.INTER_CUBIC, borderMode=cv2.BORDER_WRAP)

        # Aggiungi testo con i valori di FOV, latitudine e longitudine
        text = "FOV: {:.2f}   Latitudine: {:.2f}   Longitudine: {:.2f}".format(FOV, PHI, THETA)
        cv2.putText(persp, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
         #Restituisce l'immagine prospettica trasformata.
        return persp

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    video_name = os.path.join(current_dir, "video_1.MP4")
    eq = Equirectangular(video_name)

    while True:
        FOV = float(input("Inserisci l'angolo di campo (FOV) (1-180 gradi): "))
        if FOV < 1 or FOV > 180:
            print("L'angolo di campo deve essere compreso tra 1 e 180 gradi. Riprova.")
            continue
        
        THETA = float(input("Inserisci longitudine (-180-180 gradi): "))
        PHI = float(input("Inserisci latitudine (-90-90 gradi): "))
        if THETA < -180 or THETA > 180 or PHI < -90 or PHI > 90:
            print("La longitudine deve essere compresa tra -180 e 180 gradi, e la latitudine tra -90 e 90 gradi. Riprova.")
            continue

        height = 600
        width = 800

        # Crea una finestra a schermo intero
        cv2.namedWindow("perspective", cv2.WINDOW_NORMAL)
        #cv2.setWindowProperty("perspective", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        while True:
         #utilizza questi argomenti (fov, theta, phi, height, width) per calcolare la proiezione prospettica dell'immagine equirettangolare e 
         #applicare le trasformazioni geometriche necessarie per ottenere la vista desiderata dell'immagine. Infine, restituisce l'immagine prospettica trasformata.
            persp = eq.GetPerspective(FOV, THETA, PHI, width, height)
                
            if persp is None:
                break

            cv2.imshow("perspective", persp)
            key = cv2.waitKey(10)

            if key == ord('-'):
                FOV = min(FOV + 1, 180)

            if key == ord('+'):
                FOV = max(FOV - 1, 1)

            # Movimento della visuale
            if key == ord('a'):
                THETA -= 1
                if THETA <-180:
                    THETA = 179
            elif key == ord('d'):
                THETA += 1
                if THETA >180:
                    THETA = -179
            elif key == ord('s'):
                PHI -= 1
                if PHI < -90:
                    PHI = 89
            elif key == ord('w'):
                PHI += 1
                if PHI >90:
                    PHI = -89
            elif key == ord('q'):
                break

        cv2.destroyAllWindows()
        break