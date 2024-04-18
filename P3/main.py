from NeuronNetwork import NeuronNetwork

if __name__ == '__main__':
    neuronNetwork = NeuronNetwork()
    neuronNetwork.fit(alpha=1)
    print(neuronNetwork.make_prediction("../P3/Tests/test_language.txt"))
