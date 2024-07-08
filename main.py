import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('data/input.xlsx', engine='openpyxl')

# Crear un diccionario para almacenar los resultados
results = {}

# Iterar sobre cada fila del archivo Excel
for index, row in df.iterrows():
    cc = row['cc']
    print(f"Procesando {cc}...")
    
    # Ejecutar el scraper correspondiente
    if cc.startswith('CC1'):
        from scraper1 import scrape_cc1
        results[cc] = scrape_cc1(cc)
    elif cc.startswith('CC2'):
        from scraper2 import scrape_cc2
        results[cc] = scrape_cc2(cc)
    else:
        print(f"No se encontró un scraper para {cc}")
    
    print(f"Resultado para {cc}: {results[cc]}")