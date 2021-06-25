FROM python:3.7
WORKDIR /root
RUN mkdir /root/app

RUN pip install --no-cache-dir grpcio==1.27.2
RUN pip install --no-cache-dir scikit-learn==0.22.2.post1
RUN pip install --no-cache-dir protobuf==3.11.3

COPY server.py /root/app/server.py
COPY service_pb2_grpc.py /root/app/service_pb2_grpc.py
COPY service_pb2.py /root/app/service_pb2.py
COPY model/model.pkl /root/app/model/model.pkl

EXPOSE 8080
CMD ["python", "/root/app/server.py"]