# resource path function so pyninstaller can find images
import sys
import os


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


import tkinter as tk
from PIL import Image, ImageTk


class Grid_difficulty:
    def __init__(self, height: int, width: int, name: str):
        self.name = name
        self.height: int = height
        self.width: int = width
        self.screen_height = (self.height * 50) + 30
        self.screen_width = (self.width * 50) + 40


grid_sizes = {
    "Easy": Grid_difficulty(height=9, width=9, name="Easy"),
    "Medium": Grid_difficulty(height=16, width=16, name="Medium"),
    "Hard": Grid_difficulty(height=16, width=30, name="Hard"),
}


class Window(tk.Tk):
    def __init__(self) -> None:
        # starter coordinates for grid (from left, from top): 15,40

        super(Window, self).__init__()

        self.default_difficulty = grid_sizes["Medium"]
        self.difficulty = self.default_difficulty  # TODO change to match drop down
        self.window_width = self.default_difficulty.screen_width
        self.window_height = self.default_difficulty.screen_height
        self.geometry(f"{self.window_width}x{self.window_height}")

        # menu bar
        self.menu_bar = tk.Menu(self)
        self.difficulty_menu = tk.Menu(self, tearoff=0)
        self.difficulty_menu.add_command(
            label="Easy", command=self.set_difficulty("Easy")
        )
        self.difficulty_menu.add_command(
            label="Medium", command=self.set_difficulty("Medium")
        )
        self.difficulty_menu.add_command(
            label="Hard", command=self.set_difficulty("Hard")
        )
        self.menu_bar.add_cascade(label="Difficulty", menu=self.difficulty_menu)

        self.main_canvas = tk.Canvas(
            self, width=self.window_width, height=self.window_height
        )
        self.main_canvas.pack()

        #! >>>>>>>>>>>>>> TODO WORK ON MAKING CANVAS BOTTOM MARGIN SHOW <<<<<<<<<<<<<<<<
        self.grid_canvas = tk.Canvas(
            self,
            width=self.difficulty.width * 50,
            height=self.difficulty.height * 50,
            bg="blue",
        )
        self.grid_canvas.place(x=15,y=40)

        self.reset_button = Reset(parent=self.main_canvas)
        # self.reset_button.configure(text="Reset", command=Reset(self).reset_board)
        self.reset_button.place(x=self.window_width // 2, y=7)
        self.config(menu=self.menu_bar)

    def set_difficulty(self, dif: str):
        def inner():
            old_dif = self.difficulty.name
            new_dif = grid_sizes[dif]
            self.difficulty = new_dif
            self.geometry(f"{new_dif.screen_width}x{new_dif.screen_height}")
            #! REMOVE PRINT WHEN DONE
            print(f"changed difficulty from {old_dif} to {new_dif.name}")

        return inner


class Reset(tk.Button):
    def __init__(self, parent, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.configure(text="Reset", command=self.reset_board)
        self.parent = parent

    def reset_board(self):
        #! REMOVE PRINT HEN DONE
        print("pressed restet button")


def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()
