PROJECT="spike-sandbox"
REGION="us-central1"

ENDPOINT=$(\
  gcloud run services list \
  --project=${PROJECT} \
  --region=${REGION} \
  --platform=managed \
  --format="value(status.address.url)" \
  --filter="metadata.name=grpc-server")
ENDPOINT=${ENDPOINT#https://} && echo ${ENDPOINT}
#ENDPOINT=localhost

grpcurl \
    -proto service.proto \
    --plaintext \
    -d '{"sepal_length": 6.4, "sepal_width": 3.0, "petal_length": 5.3, "petal_width":2.3}' \
    ${ENDPOINT}:443 \
    ModelPrediction.predict