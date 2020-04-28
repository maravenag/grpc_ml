import grpc
import pickle
import numpy as np
from concurrent import futures
import service_pb2_grpc
import service_pb2
import logging

class ModelPredictionServicer(service_pb2_grpc.ModelPredictionServicer):
    def __init__(self):
        self.model = pickle.load(open("model/model.pkl", 'rb'))
    
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

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  service_pb2_grpc.add_ModelPredictionServicer_to_server(ModelPredictionServicer(), server)
  server.add_insecure_port('[::]:8080')
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()