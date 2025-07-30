# Sistema de Monitoreo IoT con Kafka y TimescaleDB

Proyecto que simula sensores IoT enviando datos en tiempo real a través de Kafka, almacenados en TimescaleDB y visualizados en Grafana.

## 🛠️ Requisitos

- Docker
- Docker Compose

## ▶️ Cómo ejecutar

1. Clona este repositorio:

```bash
## Ambas son validas
git clone https://github.com/Red33med/Iot-Monitoring.git
git clone git@github.com:Red33med/Iot-Monitoring.git

cd Iot-Monitoring
```

2. Ejecutar el script de Docker Compose en el directorio del proyecto:

```bash
docker-compose up --build
```

## 📊 Visualización de datos

1. Acceder a la interfaz de Grafana en http://localhost:3000
2. Iniciar sesión con el usuario admin y la contraseña admin
3. Crear o importar el dashboard de ejemplo

## Conectar la fuente de datos

HostURL = timescaledb:5432
Database = iotdb
User = iotuser
Password = iotpass
TLS/SSL = Disable
TimescaleDB = Activada
Lo demas por defecto




## Para detener el proyecto:

Ejecutar el script de Docker Compose en el directorio del proyecto:

```bash
docker-compose stop
```

## Eliminar los contenedores y volúmenes:

```bash
docker-compose down --volumes
```
