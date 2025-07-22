import json
import time
import psycopg2
from kafka import KafkaConsumer


def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="timescaledb",
                database="iotdb",
                user="iotuser",
                password="iotpass"
            )
            print("✅ Conectado a TimescaleDB")
            return conn
        except Exception as e:
            print(f"❌ No se pudo conectar a DB: {e}")
            time.sleep(5)

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            time TIMESTAMPTZ DEFAULT NOW(),
            sensor_id TEXT,
            temperature DOUBLE PRECISION,
            humidity DOUBLE PRECISION
        );
    """)
    # Crea hipertabla de TimescaleDB
    cursor.execute("SELECT create_hypertable('sensor_data', 'time', if_not_exists => TRUE);")
    conn.commit()
    cursor.close()

def consume_messages():
    conn = connect_db()
    create_table(conn)

    consumer = KafkaConsumer(
        'iot-sensors',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        group_id='iot-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("✅ Consumidor escuchando mensajes...")
    for message in consumer:
        data = message.value
        print(f"📥 Recibido: {data}")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sensor_data (time, sensor_id, temperature, humidity)
            VALUES (to_timestamp(%s), %s, %s, %s)
        """, (data["timestamp"], data["sensor_id"], data["temperature"], data["humidity"]))
        conn.commit()
        cursor.close()

if __name__ == "__main__":
    # Espera un poco más para asegurar que Kafka y DB estén listas
    time.sleep(15)
    consume_messages()