# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto en el que Flask escuchará
EXPOSE 5001

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
