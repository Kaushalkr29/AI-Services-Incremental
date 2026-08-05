import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class DataCleaning:
    def __init__(self, file_path, target_column):
        self.file_path = file_path
        self.target_column = target_column

    def load_data(self):
        df = pd.read_csv(self.file_path)
        df.drop(columns=["RowNumber", "CustomerId", "Surname"], inplace=True)
        return df

    def split_data(self, df):
        X = df.drop(self.target_column, axis=1)
        y = df[self.target_column]

        return train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

    def create_preprocessor(self, X_train):
        numerical_columns = X_train.select_dtypes(include=["int64", "float64"]).columns
        categorical_columns = X_train.select_dtypes(include=["object", "category"]).columns

        numerical_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler())
        ])

        categorical_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ])

        return ColumnTransformer([
            ("num", numerical_pipeline, numerical_columns),
            ("cat", categorical_pipeline, categorical_columns)
        ])