import csv
from typing import List
from collections import Counter

k_parameter: int = 0


def get_file_data(msg: str = "Provide something :) ") -> List:
    path: str = input(msg)

    with open(path, "r") as file:
        csv_reader = csv.reader(file)

        result = []
        for row in csv_reader:
            result.append(row)

    return result


def get_vector(msg: str) -> List[float]:
    user_input = input(msg)
    vector = [float(num) for num in user_input.split()]
    assert len(vector) == 4

    return vector


def process_vector(vector: List[float], train_set: List[List[float]]) -> str:
    global k_parameter

    list_of_pairs: list[dict] = []

    for i in range(0, len(train_set)):
        distance: float = ((float(train_set[i][0]) - vector[0]) ** 2 +
                           (float(train_set[i][1]) - vector[1]) ** 2 +
                           (float(train_set[i][2]) - vector[2]) ** 2 +
                           (float(train_set[i][3]) - vector[3]) ** 2)
        flower_type: str = str(train_set[i][4])
        list_of_pairs.append({"distance": distance, "type": flower_type})

    nearest_pairs = sorted(list_of_pairs, key=lambda x: x["distance"])[:k_parameter]

    counter = Counter()

    for pair in nearest_pairs:
        counter[pair["type"]] += 1

    most_common_element, _ = counter.most_common(1)[0]

    return most_common_element


def get_k_parameter(msg: str) -> int:
    k: int = int(input(msg))

    return k


if __name__ == '__main__':

    again: bool = True
    train_set = get_file_data("Provide path to train set file: ") 

    while again:
        print("1. - process single vector")
        print("2. - process test set")
        answer = input("provide option: ")
        if answer == "1":
            user_vector = get_vector("Provide vector: ")
            k_parameter = get_k_parameter("Provide K parameter: ")
            print(process_vector(vector=user_vector, train_set=train_set))
        if answer == "2":
            test_set = get_file_data("Provide path to train set: ")
            print(f"Number of elements in test set: {len(test_set)}")
            k_parameter = get_k_parameter("Provide K parameter: ")

            fail_counter: int = 0
            for row in test_set:
                vector = [float(row[0]), float(row[1]), float(row[2]), float(row[3])]
                result = process_vector(vector, train_set)
                correct_result = row[4]
                is_correct = result == correct_result
                if not is_correct:
                    fail_counter += 1
                print(f"result: {result} - correct: {correct_result}; {is_correct}")

            print(f"Number of fails = {fail_counter}, accuracy {100 - round((fail_counter*100)/len(test_set), 2)}%")

        next = input("continue? Yes/Y, No/N: ")
        if next == "No" or next == "N":
            again = False
