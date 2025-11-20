import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("COMPLETO.csv", delimiter=';')

# Limpiar los nombres de las columnas: quitar espacios y poner en mayúscula
df.columns = [col.strip().upper() for col in df.columns]

# Definir letras A-Z
letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Verificamos que todas las letras estén realmente en las columnas
letras_presentes = [letra for letra in letras if letra in df.columns]

# Calcular la suma total de letras A-Z por fila
df["TOTAL"] = df[letras_presentes].sum(axis=1)

# Calcular frecuencias relativas
for letra in letras_presentes:
    df[letra + "_REL"] = df[letra] / df["TOTAL"]

# Filtrar las secciones deseadas
secciones_objetivo = ["POLITICA", "ECONOMIA", "DEPORTES"]
df_filtrado = df[df["SECCIONES"].str.upper().isin(secciones_objetivo)]

# Graficar los histogramas de frecuencia relativa por sección
for seccion in secciones_objetivo:
    datos = df_filtrado[df_filtrado["SECCIONES"].str.upper() == seccion]
    if not datos.empty:
        frecuencias_rel = datos[letras_presentes].iloc[0] / datos[letras_presentes].iloc[0].sum()
        plt.figure(figsize=(10, 5))
        plt.bar(letras_presentes, frecuencias_rel)
        plt.title(f"Frecuencia relativa de letras - {seccion.capitalize()}")
        plt.xlabel("Letra")
        plt.ylabel("Frecuencia relativa")
        plt.ylim(0, max(frecuencias_rel) + 0.01)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
