from newspaper import Article, build
import time
import csv

# URLs de noticias (ajusta si deseas otras páginas)
urls = {
    'sitio1': 'https://www.clarin.com/',
    'sitio2': 'https://larazon.pe/',
}

TOTAL_NOTICIAS = 100
MAX_ARTICULOS_POR_SITE = 200  # para filtrar noticias vacías

noticias_totales = []
print("Extrayendo noticias...")

for sitio, url in urls.items():
    paper = build(url, memoize_articles=False)
    contador = 0
    for article in paper.articles[:MAX_ARTICULOS_POR_SITE]:
        if len(noticias_totales) >= TOTAL_NOTICIAS:
            break
        try:
            article.download()
            article.parse()
            if article.text and len(article.text.split()) > 100:
                noticias_totales.append({
                    'titulo': article.title,
                    'texto': article.text,
                    'url': article.url,
                    'seccion': sitio
                })
                contador += 1
        except:
            continue
        time.sleep(1)
    print(f"Noticias válidas extraídas de {sitio}: {contador}")

print(f"Total de noticias extraídas: {len(noticias_totales)}")

# --- Guardar directamente en CSV ---
with open('noticias_extraidasssss.csv', 'w', newline='', encoding='utf-8') as fcsv:
    writer = csv.DictWriter(fcsv, fieldnames=['url', 'titulo', 'texto', 'seccion'])
    writer.writeheader()
    for noticia in noticias_totales:
        writer.writerow(noticia)

print("Archivo CSV 'noticias_extraidas.csv' creado con éxito.")
