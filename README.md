# 🚗 Sistema de Detección Temprana de Fatiga en Conductores

Sistema de visión por computador que detecta indicadores tempranos de somnolencia en conductores (cierre de ojos, inclinación de cabeza y bostezos) mediante una cámara de video en un entorno controlado.

## 🎯 Objetivo del sistema

Implementar un modelo de detección temprana de fatiga en conductores mediante una cámara de video en un entorno controlado, utilizando **MediaPipe Face Landmark** y la extracción de características geométricas (**EAR**, **MAR**), capaz de detectar indicadores tempranos de somnolencia como el cierre de ojos, la inclinación de la cabeza y los bostezos.

## 🧠 Aplicación desarrollada

El proyecto se basa en una red neuronal convolucional **MobileNetV3Small**, de bajo costo computacional, orientada a la detección de características faciales.

Para la visión por computador se utiliza **MediaPipe Face Landmarker** (Google), integrada mediante **OpenCV** para el procesamiento de imágenes. Esta librería dibuja puntos de referencia sobre el rostro —ojos, boca, contorno, nariz, entre otros— que permiten calcular la posición de estos elementos en tiempo real.

A partir de dichos puntos se determina cuándo una persona cierra los ojos, bosteza o cabecea, mediante el cálculo de:

- **EAR** (*Eye Aspect Ratio*) — relación de aspecto del ojo
- **MAR** (*Mouth Aspect Ratio*) — relación de aspecto de la boca

La captura se realiza mediante una cámara web y las imágenes se visualizan a través de una **interfaz gráfica sencilla**.

## 🚙 Entorno de prueba (maqueta)

Para simular condiciones reales de conducción se construyó una **maqueta en forma de automóvil**, donde la cámara apunta hacia un celular que reproduce videos de personas bostezando, cerrando los ojos o cabeceando. Al detectar estos síntomas tempranos de fatiga, el sistema reproduce un **sonido de alarma**, simulando el comportamiento esperado en un vehículo real.

## 🛠️ Tecnologías utilizadas

| Componente | Herramienta |
|---|---|
| Detección de landmarks faciales | MediaPipe Face Landmarker |
| Procesamiento de imágenes | OpenCV |
| Modelo de red neuronal | MobileNetV3Small |
| Métricas de fatiga | EAR / MAR |
| Interfaz gráfica | Aplicación de escritorio/web sencilla |

## ⚙️ Funcionamiento general

1. La cámara captura el video en tiempo real.
2. MediaPipe detecta los puntos de referencia del rostro (ojos, boca, nariz, mentón, contorno).
3. Se calculan los valores de **EAR** y **MAR** en cada fotograma.
4. Si los valores indican cierre de ojos, cabeceo o bostezo sostenido, el sistema clasifica el estado como **CANSANCIO** y activa la alarma; en caso contrario, se muestra el estado **ALERTA**.

## 📄 Licencia

Proyecto académico — uso educativo.
