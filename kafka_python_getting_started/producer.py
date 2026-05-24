import json, argparse
from kafka.producer import KafkaProducer
from kafka_python_getting_started.user_data import UserData

kafka_producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def send_data(topic_name: str, data: dict, partition: int = 0):
    kafka_producer.send(topic=topic_name, value=data, partition=partition)


if __name__ == "__main__":
    # 🔹 Create parser
    parser = argparse.ArgumentParser(description="Kafka Producer CLI")

    # 🔹 Define arguments
    parser.add_argument("--topic", required=True, help="Kafka topic name")
    parser.add_argument("--user_name", required=True, help="User name")
    parser.add_argument("--location", required=True, help="User location")
    parser.add_argument("--partition", type=int, default=0, help="Partition number")

    # 🔹 Parse args
    args = parser.parse_args()

    try:
        # Create user object
        user_data = UserData(user_name=args.user_name, location=args.location).to_dict()

        # Send data
        send_data(topic_name=args.topic, data=user_data, partition=args.partition)

        print(f"✅ Sent user: {user_data}")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        kafka_producer.flush()
        kafka_producer.close()
