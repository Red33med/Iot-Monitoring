import json
import time
import random
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

TOPIC = "iot-sensors"


def create_producer():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',  # nombre del servicio Docker
                value_serializer=lambda v: json.dumps(v).encode('utf-8'), # serialización Json estandar
                api_version_auto_timeout_ms=30000  # tiempo extra para detectar versión
            )
            print("Conectado al broker Kafka")
            return producer
        except NoBrokersAvailable:
            print("Kafka no disponible, reintentando en 5 segundos...")
            time.sleep(5)

def generate_sensor_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "timestamp": int(time.time())
    }

if __name__ == "__main__":
    print("Iniciando productor... Conectándose a Kafka (kafka:9092)")
    producer = create_producer()
    print("Productor iniciado. Enviando datos cada 2 segundos...")

    try:
        while True:
            data = generate_sensor_data("sensor_001")
            print(f"Enviando: {data}")
            try:
                future = producer.send(TOPIC, value=data)
                result = future.get(timeout=10)  # confirmación de envío
            except Exception as send_error:
                print(f"Error al enviar mensaje: {send_error}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Productor detenido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        producer.close()
        print("Productor cerrado correctamente.")