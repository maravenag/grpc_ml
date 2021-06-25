import grpc
import pickle
import numpy as np
from concurrent import futures
import service_pb2_grpc
import service_pb2
import logging
import os

_PORT = os.environ["PORT"]

class ModelPredictionServicer(service_pb2_grpc.ModelPredictionServicer):
    def __init__(self):
        self.model = pickle.load(open("/root/app/model/model.pkl", 'rb'))
    
    def predict(self, request, context):
        to_predict_data = np.array([request.sepal_length,
                                    request.sepal_width,
                                    request.petal_length,
                                    request.petal_width]).reshape(1,-1)
        response = service_pb2.ModelResponse()
        try:
            prediction = self.model.predict(to_predict_data)
            response.predicted_class = prediction
            response.success = True
            return response
        except Exception as e:
            response.predicted_class = -1
            response.success = False
            return response

def serve(port:str):
    bind_address = f"[::]:{port}"
    server = grpc.server(futures.ThreadPoolExecutor())
    service_pb2_grpc.add_ModelPredictionServicer_to_server(ModelPredictionServicer(), server)
    server.add_insecure_port(bind_address)
    server.start()
    logging.info("Listening on %s.", bind_address)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve(_PORT)