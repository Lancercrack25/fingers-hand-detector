#impprtamos nuestras librerias
import cv2 
import mediapipe as mp
import numpy as np
from math import acos, degrees

#funcion para calcular las cordenadas del centro de la palma
def palma_centro(puntos_palma):
    cordenadas = np.array(puntos_palma)
    centro = np.mean(cordenadas, axis=0)
    centro = int(centro[0]), int(centro[1])
    return centro

#funcion para obtener el label de la mano (izquierda o derecha)
def get_hand_label(results, hand_index):
    if results.multi_handedness:
        return results.multi_handedness[hand_index].classification[0].label  # "Left" o "Right"
    return None

#funcion para identificar los simbolos de la mano
def simbolos_manos(dedos):
    # dedos: array de 5 booleanos [pulgar, indice, medio, anular, meñique]
    if np.array_equal(dedos, [False, True, True, False, False]):
        print(f"Simbolo de Paz ")
    elif np.array_equal(dedos, [True, True, True, True, True]):
        print(f"Simbolo de Mano Abierta")
    elif np.array_equal(dedos, [False, False, False, False, False]):
        print(f"Simbolo de Puño ")
    elif np.array_equal(dedos, [False, False, True, False, False]):
        print(f"Simbolo de dedo grosero")
    
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
contador_dedos = "_"

#array de puntos de la mano,dedos,palma, espesor de linea 
angulo_puntos_pulgar = [1, 2, 4]
puntos_palma = [0, 1, 2, 5, 9, 13, 17]
puntos_puntasdedos = [8, 12, 16, 20]
puntos_parte_inferior = [6, 10, 14, 18]
espesor_linea = [2,2,2,2,2]

#colores identificacion de tipo de dedo
verde = (48, 255, 48)
azul = (192, 101, 21)
amarillo = (8, 204, 255)
morado = (128, 64, 128)
durazno = (180, 229, 255)
# Inicializar MediaPipe Hands
with mp_hands.Hands(
    model_complexity=1,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
# Bucle de captura de video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Voltear horizontalmente el frame para una visualización más natural
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            contador_total = 0
            for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                cordenadas_puntos = []
                cordenadas_palma = []
                cordenadas_puntasdedos = []
                cordenadas_parte_inferior = []

                # Obtener el label: "Izquierda o derecha"
                hand_label = get_hand_label(results, hand_index)

                # Coordenadas del pulgar para su cálculo posterior (puntos 4 y 3)
                x4 = hand_landmarks.landmark[4].x
                x3 = hand_landmarks.landmark[3].x

                # Detecta si el pulgar está extendido según la mano
                if hand_label == "Right":
                    dedo_pulgar = np.array(x4 < x3)
                else:  # izquierda
                    dedo_pulgar = np.array(x4 > x3)
            
                #bucle para la deteccion de las cordenadas de las puntas de la mano,palma y dedos
                for i in puntos_palma:
                    x = int(hand_landmarks.landmark[i].x * width)
                    y = int(hand_landmarks.landmark[i].y * height)
                    cordenadas_palma.append((x, y))

                for i in puntos_puntasdedos:
                    x = int(hand_landmarks.landmark[i].x * width)
                    y = int(hand_landmarks.landmark[i].y * height)
                    cordenadas_puntasdedos.append([x, y])

                for i in puntos_parte_inferior:
                    x = int(hand_landmarks.landmark[i].x * width)
                    y = int(hand_landmarks.landmark[i].y * height)
                    cordenadas_parte_inferior.append([x, y])
                # Dibujar puntos de referencia de la mano
                x, y = palma_centro(cordenadas_palma)
                cv2.circle(frame, (x, y), 3, (0, 255, 0), 2)
                cordenadas_centro = np.array([x, y])
                cordenadas_puntasdedos = np.array(cordenadas_puntasdedos)
                cordenadas_parte_inferior = np.array(cordenadas_parte_inferior)
            
                if cordenadas_puntasdedos.shape[0] == 4 and cordenadas_parte_inferior.shape[0] == 4:
                    distancia_centro_punta = np.linalg.norm(cordenadas_centro - cordenadas_puntasdedos, axis=1)
                    distancia_centro_parte_inferior = np.linalg.norm(cordenadas_centro - cordenadas_parte_inferior, axis=1)
                    resta = distancia_centro_punta - distancia_centro_parte_inferior
                    dedos = resta > 0
                    dedos = np.append(dedo_pulgar, dedos)
                    contador_total += np.count_nonzero(dedos == True)

                #bucle for para determinar el espesor de la linea de cada dedo y saber si esta extendido o no
                for (i,dedo) in enumerate(dedos):
                    if dedo == True:
                        espesor_linea[i] = -1
                        simbolos_manos(dedos)
                    else:
                        espesor_linea[i] = 2
                # Dibujar mano
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            contador_dedos = str(contador_total)

        # Mostrar contador visialmente
        cv2.rectangle(frame, (0, 0), (80, 80), (120, 225, 0), -1)
        cv2.putText(frame, contador_dedos, (15, 65), 1, 5, (255, 255, 255), 2)
        #pulgar
        cv2.rectangle(frame, (100, 10), (150, 60), durazno, espesor_linea[0]) #muestra el rectangulo con su color 
        cv2.putText(frame, "Pulgar", (100, 80), 1, 1, (255, 255, 255), 2) #muestra el texto en la parte inferior del rectangulo
        #indice
        cv2.rectangle(frame, (160, 10), (210, 60), morado, espesor_linea[1]) #muestra el rectangulo con su color 
        cv2.putText(frame, "Indice", (160, 80), 1, 1, (255, 255, 255), 2)#muestra el texto en la parte inferior del rectangulo
        #medio
        cv2.rectangle(frame, (220, 10), (270, 60), amarillo, espesor_linea[2]) #muestra el rectangulo con su color 
        cv2.putText(frame, "Medio", (220, 80), 1, 1, (255, 255, 255), 2)#muestra el texto en la parte inferior del rectangulo
        #anular
        cv2.rectangle(frame, (280, 10), (330, 60), verde, espesor_linea[3]) #muestra el rectangulo con su color 
        cv2.putText(frame, "Anular", (280, 80), 1, 1, (255, 255, 255), 2)#muestra el texto en la parte inferior del rectangulo
        #meñique
        cv2.rectangle(frame, (340, 10), (390, 60), azul, espesor_linea[4]) #muestra el rectangulo con su color 
        cv2.putText(frame, "Meñique", (340, 80), 1, 1, (255, 255, 255), 2)#muestra el texto en la parte inferior del rectangulo

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
#fin del programa