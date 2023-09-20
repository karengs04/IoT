# -*- coding: utf-8 -*-
"""Esquema de comunicación- Entropía.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G82VR7VHMJmvFmgKCWMh8zX7scINNiRj
"""

pip install PyPDF2

import random
from PyPDF2 import PdfReader
import math

# Componente 1: Fuente de Información (Leer el archivo PDF)
def leer_archivo_pdf(archivo_pdf):
    pdf_reader = PdfReader(archivo_pdf)
    texto = ''
    for page in pdf_reader.pages:
        texto += page.extract_text()
    return texto

archivo_pdf = "Peter Pan.pdf"

mensaje_original = leer_archivo_pdf(archivo_pdf)

# Imprimir el mensaje original
print("Mensaje original (desde el archivo PDF): ", mensaje_original)

# Componente 2: Transmisor (Codificación a binario)
def codificar_a_binario(datos):
    return ''.join(format(ord(char), '08b') for char in datos)

datos_binarios = codificar_a_binario(mensaje_original)

# Componente 3: Canal (Simulación de ruido)
def simular_ruido(datos_binarios, rango_probabilidad=(25, 35)):
    datos_con_ruido = ''
    for bit in datos_binarios:
        if random.randint(1, 100) in range(rango_probabilidad[0], rango_probabilidad[1] + 1):
            # Cambiar el bit si el número aleatorio está dentro del rango
            datos_con_ruido += '1' if bit == '0' else '0'
        else:
            datos_con_ruido += bit
    return datos_con_ruido

datos_con_ruido = simular_ruido(datos_binarios, rango_probabilidad=(25, 35))

# Componente 4: Receptor (Decodificación desde binario)
def decodificar_desde_binario(datos_binarios):
    return ''.join(chr(int(datos_binarios[i:i+8], 2)) for i in range(0, len(datos_binarios), 8))

mensaje_recibido = decodificar_desde_binario(datos_con_ruido)
# Componente 5: Destino de Información
print("Mensaje recibido (con ruido y decodificado): ", mensaje_recibido)

# Calcular la entropía del ruido
def calcular_entropia(datos_con_ruido): #Esta función toma como entrada la secuencia de datos con ruido (datos_con_ruido), que es una cadena de bits (0 y 1).
    n = 2  # 2 símbolos posibles (0 y 1)
    # Se calculan las probabilidades de que aparezcan los dos símbolos posibles: 0 y 1. Esto se hace contando cuántas veces aparece cada símbolo en la secuencia de datos con ruido.
    # La probabilidad de 0 se calcula como la proporción de 0s en la secuencia, y la probabilidad de 1 es 1 menos la probabilidad de 0.
    probabilidad_0 = datos_con_ruido.count('0') / len(datos_con_ruido)
    probabilidad_1 = 1 - probabilidad_0
    if probabilidad_0 == 0 or probabilidad_1 == 0:
        return 0  # Entropía mínima
    entropia = -probabilidad_0 * math.log2(probabilidad_0) - probabilidad_1 * math.log2(probabilidad_1) # El logaritmo se toma en base 2 para que la entropía esté en bits.
    return entropia

entropia_ruido = calcular_entropia(datos_con_ruido)
print("Entropía del ruido en el canal: ", entropia_ruido)

print("Datos binarios originales (sin ruido):", datos_binarios)