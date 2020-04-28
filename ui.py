import streamlit as st
import service_pb2_grpc
import service_pb2
import grpc

channel = grpc.insecure_channel('[::]:8080')
stub = service_pb2_grpc.ModelPredictionStub(channel)

def main():
    st.markdown("** Iris predictions **")
    sepal_length = st.sidebar.number_input("sepal_length")
    sepal_width = st.sidebar.number_input("sepal_width")
    petal_length = st.sidebar.number_input("petal_length")
    petal_width = st.sidebar.number_input("petal_width")
    get_predictions = st.sidebar.button("Predecir")
    if get_predictions:
        features = service_pb2.ModelParams(sepal_length=sepal_length,
                                    sepal_width=sepal_width,
                                    petal_length=petal_length,
                                    petal_width=get_predictions)
        response = stub.predict(features)
        if response.success == True:
            st.markdown("***Prediction:*** {}".format(response.predicted_class))

if __name__ == "__main__":
    main()