from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from functools import partial
import pandas as pd
import pickle

def load_data(data_path: str = None) -> pd.DataFrame:
    try:
        data = pd.read_csv(data_path)
        return data
    except FileNotFoundError:
        return pd.DataFrame()

def encode_target(data: pd.DataFrame = None,
                  target: str = "species") -> pd.DataFrame:
    if target in data:
        data[target] = LabelEncoder().fit_transform(y=data[target])
        return data
    else:
        raise RuntimeError("target: {} variable not found in Dataframe".format(target))

def train_model(data: pd.DataFrame = None,
                split_ratio: float = 0.3,
                target: str = "species"):
    train, test = train_test_split(data, test_size=split_ratio)
    model_params = {
        "n_estimators": 100,
        "max_depth":8,
        "min_samples_split":4,
        "min_samples_leaf":2,
    }
    training_cols = [col for col in train.columns if col != target]
    model = RandomForestClassifier(**model_params)
    model.fit(X=train[training_cols],y=train[target])
    return model, train, test

def evaluate_model(model: RandomForestClassifier,
                   test_data: pd.DataFrame,
                   target: str = "species"):
    testing_cols = [col for col in test_data.columns if col != target]
    predictions = model.predict(test_data[testing_cols])
    real_values = test_data[target]
    print("accuracy: ", accuracy_score(y_true=real_values, y_pred=predictions))

if __name__ == "__main__":
    data = load_data(data_path="data/data.csv")
    processed_data = encode_target(data)
    print(processed_data.head())
    model, train, test = train_model(data=data, split_ratio=0.4)
    evaluate_model(model, test_data=test)
    pickle.dump(model, open("model/model.pkl", 'wb'))