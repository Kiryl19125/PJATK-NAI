from model import *
from view import Tag, create_ui
import dearpygui.dearpygui as dpg
import xdialog

perceptron: Perceptron = NotImplemented


def init_controller() -> None:
    dpg.set_item_callback(Tag.load_train_file_button, load_train_file)
    dpg.set_item_callback(Tag.load_test_file_button, load_test_file)
    dpg.set_item_callback(Tag.fit_axis_button, callback=fit_axis)
    dpg.set_item_callback(Tag.make_prediction_button, callback=make_prediction)


def init_view() -> None:
    create_ui()


def load_train_file():
    global perceptron
    path: str = xdialog.open_file(title="Select train file", filetypes=[("csv files", "*.csv")])
    perceptron = Perceptron(threshold=dpg.get_value(Tag.threshold_input),
                            default_weight_value=dpg.get_value(Tag.weight_input))
    perceptron.fit(path, alpha=dpg.get_value(Tag.alpha_input))

    weights = ""

    for child in dpg.get_item_children(Tag.weights_y_axis)[1]:
        dpg.delete_item(child)

    for child in dpg.get_item_children(Tag.threshold_y_axis)[1]:
        dpg.delete_item(child)

    for i in range(len(perceptron.weights)):
        weights += f"{perceptron.weights[i]}, "
        dpg.add_bar_series(x=[i], y=[perceptron.weights[i]], label=f"Weight {i}", parent=Tag.weights_y_axis)

    dpg.add_bar_series(x=[i + 1], y=[perceptron.threshold], label="Threshold", parent=Tag.threshold_y_axis)

    dpg.set_value(Tag.weights_text, weights)
    dpg.set_value(Tag.threshold_text, perceptron.threshold)

    fit_axis()


def load_test_file():
    path = xdialog.open_file(title="Select train file", filetypes=[("csv files", "*.csv")])
    input_data, desired = read_file(path)

    result_str = ""
    error_counter = 0
    for i in range(len(input_data)):
        predict: Flower = perceptron.make_prediction(vector=input_data[i])
        result_str += f"{predict.name} - {desired[i]} - {predict.value == desired[i]}\n"
        if not predict.value == desired[i]:
            error_counter += 1

    accuracy = 100 - (error_counter * 100) / len(input_data)
    result_str += f"Accuracy = {accuracy}%\n"

    dpg.set_value(item=Tag.result_str, value=result_str)


def make_prediction():
    vector_str: str = dpg.get_value(Tag.vector_input)
    vector: Vector = [float(num) for num in vector_str.split(",")]
    result = perceptron.make_prediction(vector)
    dpg.set_value(Tag.result_str, result.name)


def fit_axis():
    dpg.fit_axis_data(Tag.threshold_y_axis),
    dpg.fit_axis_data(Tag.weights_y_axis),
    dpg.fit_axis_data(Tag.x_axis)
