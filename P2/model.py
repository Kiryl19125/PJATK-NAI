import csv
from typing import Tuple, List
from enum import Enum

Matrix = List[List[float]]
Vector = List[float]


def scalar(vector_1: Vector, vector_2: Vector) -> float:
    assert len(vector_1) == len(vector_2)

    output: float = 0
    for i in range(len(vector_1)):
        output += vector_1[i] * vector_2[i]

    return output


def multiply_vector(vector: Vector, multiplier: float) -> Vector:
    output: Vector = []
    for num in vector:
        output.append(num * multiplier)

    return output


def vector_sum(vector_1: Vector, vector_2: Vector) -> Vector:
    assert len(vector_1) == len(vector_2)

    output: Vector = []
    for i in range(len(vector_1)):
        output.append(vector_1[i] + vector_2[i])

    return output


def read_file(path: str) -> Tuple[Matrix, Vector]:
    with open(path, "r") as file:
        reader = csv.reader(file)

        parameters: Matrix = []
        desired: Vector = []
        for row in reader:
            parameters.append([float(num) for num in row[:-1]])
            desired.append(Flower.Iris_setosa.value if row[-1] == "Iris-setosa" else Flower.Iris_versicolor.value)

    return parameters, desired


class Flower(Enum):
    Iris_versicolor = 0
    Iris_setosa = 1


class Perceptron:
    weights: Vector = []

    def __init__(self, threshold: float = 1, default_weight_value: float = 0.5):
        self.threshold = threshold
        self.default_weight_value = default_weight_value

    def fit(self, path: str, alpha: float) -> None:
        input_data, desired = read_file(path)

        assert len(input_data) == len(desired)

        # init weight
        self.weights.clear()
        for _ in range(len(input_data[0])):
            self.weights.append(self.default_weight_value)

        for i in range(len(input_data)):
            # make prediction
            prediction = self.make_prediction(input_data[i])

            self.__adjust_threshold(prediction.value, desired[i], alpha)

            self.__adjust_weight(input_data[i], alpha, desired[i], prediction.value)

    def __adjust_threshold(self, prediction: float, desired: float, alpha: float) -> None:
        self.threshold += (prediction - desired) * alpha

    def __adjust_weight(self, vector: Vector, alpha: float, desired: float, prediction: float) -> None:
        alpha_mult_input: Vector = multiply_vector(vector, alpha)
        delta_mult_alpha: Vector = multiply_vector(alpha_mult_input, desired - prediction)
        self.weights = vector_sum(self.weights, delta_mult_alpha)

    def make_prediction(self, vector: Vector) -> Flower:
        assert len(vector) == len(self.weights)

        if scalar(vector, self.weights) >= self.threshold:
            return Flower.Iris_setosa
        else:
            return Flower.Iris_versicolor
