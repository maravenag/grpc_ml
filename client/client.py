import service_pb2_grpc
import service_pb2
import logging
import grpc
import sys
import time
import requests as re
import os

GRPC_SERVER_ADDRESS = os.environ["GRPC_SERVER_ADDRESS"]
CHANNEL = grpc.insecure_channel(f'{GRPC_SERVER_ADDRESS}:8080')

def main():
    stub = service_pb2_grpc.ModelPredictionStub(CHANNEL)

    features = service_pb2.ModelParams(sepal_length=6.4,
                                       sepal_width=3.2,
                                       petal_length=5.3,
                                       petal_width=2.3)
    response = stub.predict(features)
    print(type(response))
    print("status:",response.success)
    print("prediction:", response.predicted_class)

if __name__ == "__main__":
    main()