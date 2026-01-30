# 🧠 Agente Recomendador de Productos

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
 ## 🏗️ Arquitectura General
El sistema se compone de los siguientes módulos:
Interfaz gráfica (GUI): desarrollada con CustomTkinter, permite la interacción con el usuario.
Módulo de análisis de consumo: procesa datos históricos y patrones de uso.
Motor de recomendación: aplica el algoritmo de escalas para sugerir cambios de plan.
Módulo de persuasión: genera mensajes personalizados para recomendar planes superiores.
Cierre de conversación: incluye análisis de sentimiento, resumen y propuesta final.
 ##  💻 Tecnologías Usadas
 Python 3.x

CustomTkinter para la interfaz gráfica.

PIL (Pillow) para manejo de imágenes.

LangChain + Google Generative AI para procesamiento de lenguaje natural.

Tkinter para componentes básicos de GUI.
## ⚙️ Instalación y Ejecución
