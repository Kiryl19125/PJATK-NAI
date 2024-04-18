from controller import *


def main() -> None:
    dpg.create_context()

    init_view()
    init_controller()

    dpg.create_viewport(title='Project 2', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(Tag.main_window, True)
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
