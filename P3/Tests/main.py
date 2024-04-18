# from P3.file_service import *
from P3.Neuron import Neuron, get_input_vector, count_letters, read_file

if __name__ == '__main__':

    neuron = Neuron(language="english")
    neuron.fit(alpha=1)

    input_vector = get_input_vector(count_letters(read_file("../../P3/languages/english/english_text_2.txt")))

    print(neuron.make_prediction(input_vector))


