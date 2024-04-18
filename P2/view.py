import dearpygui.dearpygui as dpg


class Tag:
    main_window = "main_window"
    load_train_file_button = "load_train_file_button"
    load_test_file_button = "load_test_file_button"
    fit_axis_button = "fit_axis_button"
    weights_y_axis = "weights_y_axis"
    threshold_y_axis = "threshold_y_axis"
    x_axis = "x_axis"
    weights_text = "weights_text"
    threshold_text = "threshold_text"

    alpha_input = "alpha_input"
    weight_input = "weight_input"
    threshold_input = "threshold_input"

    result_str = "result_str"

    vector_input = "vector_input"
    make_prediction_button = "make_prediction_button"


def create_ui() -> None:
    with dpg.window(tag=Tag.main_window):
        with dpg.table(header_row=False, resizable=True):
            dpg.add_table_column(init_width_or_weight=40)
            dpg.add_table_column(init_width_or_weight=60)
            with dpg.table_row():
                with dpg.table_cell():
                    with dpg.child_window(height=-2):
                        with dpg.group(horizontal=True):
                            dpg.add_button(label="Load train file", width=120, tag=Tag.load_train_file_button)
                            dpg.add_button(label="Load test file", width=120, tag=Tag.load_test_file_button)
                        dpg.add_input_float(label="Alpha", tag=Tag.alpha_input, default_value=0.1, step=0.001)
                        dpg.add_input_float(label="Dfault weight value", tag=Tag.weight_input, default_value=0.5,
                                            step=0.001)
                        dpg.add_input_float(label="Default threshold", tag=Tag.threshold_input, default_value=1,
                                            step=0.001)

                        with dpg.group(horizontal=True):
                            dpg.add_input_text(label="Vector input", width=-250, tag=Tag.vector_input)
                            dpg.add_button(label="Make prediction", width=125, tag=Tag.make_prediction_button)

                        with dpg.child_window(width=-1, height=-2):
                            dpg.add_text(tag=Tag.result_str)

                with dpg.table_cell():
                    with dpg.child_window(height=-2):
                        dpg.add_button(label="Fit Axis", width=75, tag=Tag.fit_axis_button)
                        with dpg.plot(width=-1, height=-50):
                            dpg.add_plot_legend()
                            # create x axis
                            dpg.add_plot_axis(dpg.mvXAxis, label="x", tag=Tag.x_axis)
                            dpg.add_plot_axis(dpg.mvYAxis, label="Weights", tag=Tag.weights_y_axis)
                            dpg.add_plot_axis(dpg.mvYAxis, label="Threshold", tag=Tag.threshold_y_axis)
                        dpg.add_separator()
                        with dpg.group(horizontal=True):
                            dpg.add_text("Weights:")
                            dpg.add_text(tag=Tag.weights_text)
                        with dpg.group(horizontal=True):
                            dpg.add_text("Threshold:")
                            dpg.add_text(tag=Tag.threshold_text)
