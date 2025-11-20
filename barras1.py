import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Cargar los datos
noticias_df = pd.read_csv('frecuencia_noticias123.csv')
referencia_df = pd.read_csv('COMPLETO.csv', delimiter=';')

# Normalizar columnas
letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
noticias_df.columns = [col.strip().upper() for col in noticias_df.columns]
referencia_df.columns = [col.strip().upper() for col in referencia_df.columns]

# Calcular frecuencias relativas para noticias
noticias_df['TOTAL'] = noticias_df[letras].sum(axis=1)
for letra in letras:
    noticias_df[letra + '_REL'] = noticias_df[letra] / noticias_df['TOTAL']

# Calcular frecuencias relativas para las secciones de referencia
secciones_ref = ['POLITICA', 'ECONOMIA', 'DEPORTES']
ref_relativas = {}

for seccion in secciones_ref:
    datos = referencia_df[referencia_df['SECCIONES'].str.upper() == seccion]
    suma = datos[letras].sum()
    total = suma.sum()
    ref_relativas[seccion] = (suma / total).values

# Establecer el umbral
UMBRAL_CHI2 = 0.30

# Comparar cada noticia
for i, row in noticias_df.iterrows():
    rel_noticia = [row[letra + '_REL'] for letra in letras]
    
    chi2_resultados = {}
    for seccion in secciones_ref:
        chi2_valor = chisquare(f_obs=rel_noticia, f_exp=ref_relativas[seccion])[0]
        chi2_resultados[seccion] = chi2_valor

    # Obtener sección con menor chi²
    seccion_mas_cercana = min(chi2_resultados, key=chi2_resultados.get)
    valor_chi2_min = chi2_resultados[seccion_mas_cercana]

    # Verificar si pasa el umbral
    if valor_chi2_min <= UMBRAL_CHI2:
        clasificacion = seccion_mas_cercana
    else:
        clasificacion = 'INDEFINIDO'

    print(f"Noticia {i+1}: Clasificada como {clasificacion} (Chi² = {valor_chi2_min:.4f})")

    # Graficar comparativo
    x = np.arange(len(letras))
    ancho = 0.2

    plt.figure(figsize=(12, 5))
    plt.bar(x - 1.5*ancho, rel_noticia, width=ancho, label='Noticia', color='black')
    for idx, seccion in enumerate(secciones_ref):
        plt.bar(x + (idx - 0.5)*ancho, ref_relativas[seccion], width=ancho, label=seccion.capitalize())

    plt.xticks(x, letras)
    plt.ylim(0, max(max(rel_noticia), *(max(ref_relativas[s]) for s in secciones_ref)) + 0.01)
    url = row['URL']
    plt.title(f'Clasificación: {clasificacion} (Chi² = {valor_chi2_min:.4f})\n{url}', fontsize=10)
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.tight_layout()
    plt.grid(True, axis='y', linestyle='--', alpha=0.3)
    plt.show()
