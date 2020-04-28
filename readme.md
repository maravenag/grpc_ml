```
python -m grpc_tools.protoc \
      -I=/Users/maravenag/Desktop/gRCP_in_action/ \
      --python_out=. \
      --grpc_python_out=. \
      service.proto
```