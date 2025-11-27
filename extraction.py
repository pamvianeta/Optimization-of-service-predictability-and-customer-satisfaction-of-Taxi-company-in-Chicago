# Obtener el contenido de la página
url = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
response = requests.get(url)

# Convertir el contenido HTML a texto
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar la tabla específica usando el atributo 'id'
table = soup.find('table', attrs={"id": "weather_records"})

# 1. Extraer los encabezados de la tabla (columnas)
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# 2. Extraer las filas de datos
data = []
for row in table.find_all('tr')[1:]:  # Omitir la fila de encabezado que ya extrajimos
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    if row_data:
        data.append(row_data)

# 3. Crear y mostrar el DataFrame 
weather_records = pd.DataFrame(data, columns=headers)
print(weather_records)
