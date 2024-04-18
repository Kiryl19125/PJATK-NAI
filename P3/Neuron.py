from file_service import *

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


def vector_sub(vector_1: Vector, vector_2: Vector) -> Vector:
    assert len(vector_1) == len(vector_2)

    output: Vector = []
    for i in range(len(vector_1)):
        output.append(vector_1[i] - vector_2[i])

    return output


class Neuron:
    weights = []

    def __init__(self, language: str, default_threshold: float = 1, default_weight_value: float = 0.5):
        self.threshold = default_threshold
        self.default_weight_value = default_weight_value
        self.language = language
        self.__init_weights()

    def fit(self, alpha: float = 1):
        self.__init_weights()
        for run in range(100):
            files = get_txt_files()
            for file in files:
                total, letters_count = count_letters(read_file(str(file)))
                input_vector = get_input_vector(total=total, data=letters_count)
                prediction = self.make_prediction(input_vector)
                desired = 1 if self.language in str(file) else 0
                self.__adjust_threshold(prediction, desired, alpha)
                self.__adjust_weight(input_vector, alpha, desired, prediction)

    def __init_weights(self):
        self.weights.clear()
        for _ in range(26):
            self.weights.append(self.default_weight_value)

    def __adjust_threshold(self, prediction: float, desired: float, alpha: float) -> None:
        self.threshold += (prediction - desired) * alpha

    def __adjust_weight(self, vector: Vector, alpha: float, desired: float, prediction: float) -> None:
        alpha_mult_input: Vector = multiply_vector(vector, alpha)
        delta_mult_alpha: Vector = multiply_vector(alpha_mult_input, desired - prediction)
        self.weights = vector_sum(self.weights, delta_mult_alpha)

    def make_prediction(self, vector: Vector) -> float:
        assert len(vector) == len(self.weights)

        if scalar(vector, self.weights) >= self.threshold:
            return 1
        else:
            return 0
