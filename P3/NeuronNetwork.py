from P3.Neuron import Neuron
from P3.file_service import *


class NeuronNetwork:

    def __init__(self):
        self.english_neuron = Neuron(language="english")
        self.german_neuron = Neuron(language="german")
        self.polish_neuron = Neuron(language="polish")

    def fit(self, alpha: float = 1):
        self.english_neuron.fit(alpha)
        self.german_neuron.fit(alpha)
        self.polish_neuron.fit(alpha)

    def make_prediction(self, file_path: str) -> str:
        text = read_file(file_path)
        total, letters_count = count_letters(text)
        input_vector = get_input_vector(total, letters_count)

        if self.english_neuron.make_prediction(input_vector) == 1:
            return "english"
        elif self.german_neuron.make_prediction(input_vector) == 1:
            return "german"
        elif self.polish_neuron.make_prediction(input_vector) == 1:
            return "polish"
        else:
            return "unknown language"
