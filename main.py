import json
from kafka import KafkaProducer

folderName = "~/kafkaCerts/kafka-pizza/"
producer = KafkaProducer(
    security_protocol="SSL",
    ssl_cafile="kafka-2b54e506"+"ca.pem",
    ssl_certfile="kafka-2b54e506"+"service.cert",
    ssl_keyfile="kafka-2b54e506"+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')

)

producer.send("test-topic",
                key={"key": 1},
                value={"message": "hello world"}
            )
producer.flush()