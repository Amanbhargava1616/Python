from kafka.admin import KafkaAdminClient, NewTopic
from typing import Tuple, List

kafka_admin = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="delivery-app",
)


def create_topic(topic_tuple: List[Tuple[str, int, int]]):
    kafka_admin.create_topics(
        new_topics=[
            NewTopic(
                name=name,
                num_partitions=partition,
                replication_factor=replication_factor,
            )
            for name, partition, replication_factor in topic_tuple
        ]
    )


if __name__ == "__main__":
    # Create topic
    try:
        create_topic(
            [
                ("riders", 1, 1),
                ("orders", 2, 1),
            ]
        )
        print(f"✅ Topics created")
    except Exception as e:
        print("❌ Error creating topic:", e)
    finally:
        kafka_admin.close()
