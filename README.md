<h1 style="color: #2ecc71; font-size: 48px;">Contador-detector dedos de manos </h1>
<img width="705" height="465" alt="images" src="https://github.com/user-attachments/assets/79f713b3-2fe2-46bd-9b72-1e3eca52d012" /><br>
Este proyecto fue desarrollado utilizando **OpenCV** y el modelo preentrenado **MediaPipe Hands** de Google.  
Su objetivo es detectar en tiempo real:

- ✋ Cuántos dedos están levantados
- 🖐️ Cuáles dedos están levantados (identificación individual)
- 🤙 Reconocimiento básico de gestos manuales

El sistema realiza el análisis a partir de la posición de los landmarks generados por MediaPipe, lo que permite interpretar movimientos y gestos de forma eficiente y precisa.<br>

<video width="340" height="360" src ="https://github.com/user-attachments/assets/6c6ce2e0-8069-4951-9fe5-997fa78e7b31"><br>

<h1 style="color: #2ecc71; font-size: 48px;"> Ambas manos</h1>
El programa tiene la funcionalidad de contar no solamente los dedos y que dedos estan levantados de una sola mano, si no de ambas manos
<img width="1547" height="619" alt="resultado 2" src="https://github.com/user-attachments/assets/6639cc74-2763-4025-9b18-2c1df1dfaab8" /><br>
<h1 style="color: #2ecc71; font-size: 48px;">Modelo mediapipe</h1>
Google Open Source ha desarrollado más de 2000 proyectos Open Source que podemos explorar en su página oficial (https://opensource.google/). Precisamente uno de esos proyectos es el que veremos como instalar hoy, MediaPipe. 

Este es un framework multimodal y multiplataforma que aplica machine learning, permitiéndonos desarrollar proyectos o aplicaciones en dispositivos móviles, de escritorio o en la web. 

Pero, ¿qué tiene de bueno este framework?, pues posee modelos de machine learning, para la detección de rostro, trancking de manos, segmentación de cabello, detección y trackeo de objetos e incluso detección y tracking de objetos 3D. Y estos son solo algunos. 

Además, uno pensaría que al aplicar estos modelos, el resultado de las detecciones sería lento. Pero no, de hecho es de lo más sorprendente, ya que nos permite correr programas desde la CPU, y con un muy buen desempeño. 

MediaPipe está disponible para Android, iOS, c++, Python, Javascript y Coral. Pero hay que tomar en cuenta que no todas las soluciones están disponibles para todos ellos, de hecho a continuación tenemos la tabla de información que nos provee la web oficial hasta el momento. 


<img width="705" height="465" alt="images" src="https://github.com/user-attachments/assets/b61e8a1d-e4d0-4457-a19c-6ae160d4e78d" /><br>
<h1 style="color: #2ecc71; font-size: 48px;">Gestos que identifica el proyecto</h1>
Los gestos que puede identificar este detector de manos y dedos son los siguientes:

-Paz

-Mano abierta

-Dedo grosero

-Puño cerrado

<h1 style="color: #2ecc71; font-size: 48px;">Liberias usadas</h1>
-cv2

-mediapipe

-numpy

-math

comando para instalacion de algunas de estas librerias: pip install opencv-python mediapipe numpy

<h1 style="color: #2ecc71; font-size: 48px;">Recomendaciones</h1>
para una mejor depuracion y ejecucion del proyecto recomiendo la creacion de un entorno virtual, el cual permite descargar librerias unicamente para el proyecto, evitando errores y porblemas con otros proyectos y liberias globales
aqui dejo unos pasos para la creacion de un entorno virtual:

-accede a la ruta de tu proyecto utilizando el comando cd

-Una vez dentro de la ruta ejecuta el siguiente comando: python -m venv nombre_entorno

-Ya creado tu entorno virtual deberas de activarlo con el siguiente conmando: nombre_entorno\Scripts\activate

-Para saber si se activo correctamente simplemente verifica que el nombre del entorno se encuentre al lado(izquierdo) entre parentesis de tu ruta del proyecto

-Instala las liberias necesarias para tu proyecto, utilizando pip install nombre libreria

-Si deseas desactivarlo simplemente ejecuta: deactivate








