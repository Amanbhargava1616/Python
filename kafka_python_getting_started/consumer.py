import argparse, json
from kafka.consumer import KafkaConsumer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kafka Consumer CLI")

    parser.add_argument("--topic", required=True, help="Kafka topic name")
    parser.add_argument("--group_id", required=True, help="Consumer group ID")

    args = parser.parse_args()

    kafka_consumer = None

    try:
        kafka_consumer = KafkaConsumer(
            args.topic,
            bootstrap_servers="localhost:9092",
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=args.group_id,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )

        print(f"✅ Listening to topic '{args.topic}'...")

        for message in kafka_consumer:
            print(f"📩 Received: {message.value}")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if kafka_consumer:
            kafka_consumer.close()
