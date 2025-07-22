# Sistema de Monitoreo IoT con Kafka y TimescaleDB

Proyecto que simula sensores IoT enviando datos en tiempo real a través de Kafka, almacenados en TimescaleDB y visualizados en Grafana.

## 🛠️ Requisitos

- Docker
- Docker Compose

## ▶️ Cómo ejecutar

1. Clona este repositorio:

```bash
git clone https://github.com/Red33med/iot-monitoring.git
cd iot-monitoring
```

2. Ejecutar el script de Docker Compose en el directorio del proyecto:

```bash
docker-compose up --build
```

## 📊 Visualización de datos

1. Acceder a la interfaz de Grafana en http://localhost:3000
2. Iniciar sesión con el usuario admin y la contraseña admin
3. Crear o importar el dashboard de ejemplo

## Para detener el proyecto:

Ejecutar el script de Docker Compose en el directorio del proyecto:

```bash
docker-compose stop
```

## Eliminar los contenedores y volúmenes:

```bash
docker-compose down --volumes
```
