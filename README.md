# 🧠 Agente Recomendador de Productos

<img width="250" height="200" alt="bitcore_logo" src="https://github.com/user-attachments/assets/65eccc45-f6c1-42fd-b23f-dff560330d7e" />

## 📌 Objetivo
Recomendar productos y planes de internet según el **CONSUMO del cliente**, analizando velocidad, histórico y patrones de uso para generar ofertas personalizadas y propuestas de cambio de plan.

## 📝 Descripción
Este proyecto implementa un **Agente Inteligente** que:
- Analiza el consumo de internet del cliente.
- Genera recomendaciones de planes y productos.
- Persuade al cliente hacia planes de mayor costo cuando el perfil lo justifica.
- Utiliza un algoritmo de "escalas" para proponer cambios progresivos de plan.
- Cierra la interacción con un detalle final: análisis de sentimiento, resumen de la conversación, plan propuesto y motivo de la recomendación.

## ✅ Requisitos Mínimos
1. Correcto análisis del consumo de internet del cliente.
2. Propuesta de cambio de plan de internet.
3. Persuasión para recomendar un plan de mayor costo cuando aplique.
4. Implementación de un algoritmo de "escalas" para el cambio de plan.
5. Cierre con detalle final de la conversación:
   - Análisis de sentimiento  
   - Resumen de la conversación  
   - Plan propuesto  
   - Motivo de la recomendación  

## 🛠️ Librerías utilizadas
```python
import os
import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import messagebox
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
```
 ## 🏗️ Arquitectura General
El sistema se compone de los siguientes módulos:
Interfaz gráfica (GUI): desarrollada con CustomTkinter, permite la interacción con el usuario.
Módulo de análisis de consumo: procesa datos históricos y patrones de uso.
Motor de recomendación: aplica el algoritmo de escalas para sugerir cambios de plan.
Módulo de persuasión: genera mensajes personalizados para recomendar planes superiores.
Cierre de conversación: incluye análisis de sentimiento, resumen y propuesta final.
 ## 💻 Tecnologías Usadas
 Python 3.x

CustomTkinter para la interfaz gráfica.

PIL (Pillow) para manejo de imágenes.

LangChain + Google Generative AI para procesamiento de lenguaje natural.

Tkinter para componentes básicos de GUI.
## ⚙️ Instalación y Ejecución
1.Clonar el repositorio: 
```bash
git clone https://github.com/juanHernandezbit-prog/Semillero_IA_Proyecto_Agente_Recomendador_BitCoreAI/tree/main
```
2.Entrar en la carpeta del proyecto:
```bash
cd Semillero_IA_Proyecto_Agente_Recomendador_BitCoreAI
```
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecutar el sistema:
```bash
python main.py
```
 ## ▶️ Uso del Sistema
El usuario ingresa datos de consumo de internet.

El agente analiza velocidad y patrones de uso.

Se genera una recomendación de plan acorde al perfil.

Se aplica el algoritmo de escalas para sugerir un plan superior si corresponde.

El sistema muestra un cierre detallado con:

Análisis de sentimiento

Resumen de la conversación

Plan propuesto

Motivo de la recomendación

 ## 👥 Autores
 Juan Pablo Hernández Arámbulo (@juanHernandezbit-prog)
 

Jessie Gabriela Suárez Naranjo (@jessiesuarez)

## link del video

https://drive.google.com/file/d/15YngrUVEluXu-XNj3wiKLN5Z03tyMxCA/view?usp=sharing
 


