from pathlib import Path

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from pomegranate.BayesianNetwork import BayesianNetwork


def read_data(dataset_path: Path) -> (pd.DataFrame, pd.DataFrame):
    df = pd.read_csv(dataset_path)
    # TODO make it more robustness and add more features
    df = df.dropna()
    df = df[['Survived', 'Pclass', 'Sex', 'SibSp']]
    df['Sex'] = [1 if x == 'male' else 0 for x in df['Sex']]

    # TODO use cross validation
    train, val = train_test_split(df)
    return train, val


def error(input_data_frame: pd.DataFrame, network: BayesianNetwork) -> str:
    input_data_frame_copy = input_data_frame.copy()
    input_data_frame_copy['Survived'] = [None] * input_data_frame_copy.shape[0]

    pred = network.predict(input_data_frame_copy.values, check_input=False)
    pred = np.array(pred)

    y_pred = pred[:, 0]
    y_real = input_data_frame['Survived'].values

    return classification_report(y_true=y_real.astype(int), y_pred=y_pred.astype(int))


def main():
    train_path = Path('./data/train.csv')
    train_data, val_data = read_data(train_path)

    bayesian_network = BayesianNetwork.from_samples(train_data.values, state_names=train_data.columns)

    classification_report_train = error(train_data, bayesian_network)
    classification_report_val = error(val_data, bayesian_network)
    print("train\n{}".format(classification_report_train))
    print("validation\n{}".format(classification_report_val))


if __name__ == '__main__':
    main()
