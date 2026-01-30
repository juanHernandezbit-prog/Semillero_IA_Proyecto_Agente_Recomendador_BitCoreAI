import os
import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import messagebox
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# CONFIGURACIÓN
os.environ["GOOGLE_API_KEY"] = "INGRESA TU API"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.6 
)

lista_planes = [200, 350, 500, 1000]

prompt_vendedor = """
Eres un Agente Experto en Telecomunicaciones (Analista de Datos + Vendedor).
Tu tarea es analizar los datos crudos de un cliente y decidir autónomamente la mejor estrategia.

DATOS DEL CLIENTE:
{datos_cliente}

CATÁLOGO DE PLANES DISPONIBLES (Mbps):
{planes}

TUS INSTRUCCIONES DE RAZONAMIENTO:
1. ANÁLISIS DE CONSUMO: Compara el último mes del historial con su plan actual. ¿Está saturado (usa más del 90%)?
   - Si NO está saturado: Tu respuesta final debe ser "CLIENTE_OK".
   - Si SÍ está saturado: Debes recomendar el SIGUIENTE plan de la lista (upgrade).

2. PERFILADO DE USUARIO: Mira las 'apps_frecuentes' y el 'horario_pico'.
   - Deduce qué tipo de usuario es (Gamer, Home Office, Estudiante, etc.) y úsalo para tu argumento.

3. GENERACIÓN DEL MENSAJE:
   - Si hay saturación, escribe un mensaje corto y persuasivo (SMS/WhatsApp).
   - Usa el perfil detectado para dar un argumento personalizado.
   - Sé directo y saluda por el nombre.

FORMATO DE SALIDA:
[ANÁLISIS]: ...
[MENSAJE]: ...
"""

prompt = PromptTemplate.from_template(prompt_vendedor)
chain = prompt | llm

# ---------------- GUI ----------------
def procesar_cliente():
    try:
        nombre = entry_nombre.get()
        plan = int(entry_plan.get())
        historial = [int(x.strip()) for x in entry_historial.get().split(",")]
        apps = [x.strip() for x in entry_apps.get().split(",")]
        horario = entry_horario.get()

        cliente = {
            'nombre': nombre,
            'plan_actual_mbps': plan,
            'historial_consumo': historial,
            'apps_frecuentes': apps,
            'horario_pico': horario
        }

        respuesta = chain.invoke({
            "datos_cliente": str(cliente),
            "planes": str(lista_planes)
        })

        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, respuesta.content)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema: {e}")

# Ventana principal
ventana = tk.Tk()
ventana.title("SISTEMA DE VENTAS - INGRESO DE DATOS")

# --- Logo ---
logo_img = ctk.CTkImage(light_image=Image.open("bitcore_logo.png"), size=(100, 100))
logo_label = ctk.CTkLabel(ventana, image=logo_img, text="")
logo_label.place(x=8, y=10)

# --- Interfaz ---
tk.Label(ventana, text="Nombre del Cliente:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Plan Actual (Mbps):").pack()
entry_plan = tk.Entry(ventana)
entry_plan.pack()

tk.Label(ventana, text="Historial de Consumo (ej: 200,250,310):").pack()
entry_historial = tk.Entry(ventana)
entry_historial.pack()

tk.Label(ventana, text="Apps Frecuentes (ej: Netflix, Zoom, Juegos):").pack()
entry_apps = tk.Entry(ventana)
entry_apps.pack()

tk.Label(ventana, text="Horario Pico (ej: Noche, Tarde , Dia):").pack()
entry_horario = tk.Entry(ventana)
entry_horario.pack()

btn_procesar = tk.Button(ventana, text="Procesar con IA", command=procesar_cliente)
btn_procesar.pack(pady=10)

text_resultado = tk.Text(ventana, height=10, width=100)
text_resultado.pack()

ventana.mainloop()

