import tkinter as tk
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage


class GridDifficulty:
    """
    grid size data for a given difficulty
    """

    def __init__(self, height: int, width: int, name: str):
        self.name = name
        self.height: int = height
        self.width: int = width
        self.screen_height = (self.height * 25) + 60
        self.screen_width = (self.width * 25) + 40


# hard coded grid sizes
grid_sizes = {
    "Easy": GridDifficulty(height=9, width=9, name="Easy"),
    "Medium": GridDifficulty(height=16, width=16, name="Medium"),
    "Hard": GridDifficulty(height=16, width=30, name="Hard"),
}


class Window(tk.Tk):
    """
    Main game window
    """

    def __init__(self) -> None:
        # starter coordinates for grid (from left, from top): 15,40

        super(Window, self).__init__()

        self.grid_sqr_image = ImageTk.PhotoImage(
            Image.open("./images/grid_square1.png").resize(
                (25, 25), Image.Resampling.LANCZOS
            )
        )
        self.flag_image = ImageTk.PhotoImage(
            Image.open("./images/grid_flag1.png").resize(
                (25, 25), Image.Resampling.LANCZOS
            )
        )

        self.default_difficulty = grid_sizes["Medium"]
        self.difficulty = self.default_difficulty
        self.window_width = self.difficulty.screen_width
        self.window_height = self.difficulty.screen_height
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
            width=self.difficulty.width * 25,
            height=self.difficulty.height * 25,
            bg="blue",
        )
        self.grid_canvas.place(x=15, y=40)

        self.reset_button = Reset(parent=self.main_canvas)
        self.reset_button.place(x=self.window_width // 2, y=21, anchor="center")
        self.config(menu=self.menu_bar)

    def set_difficulty(self, dif: str):
        def inner():
            old_dif = self.difficulty.name
            new_dif = grid_sizes[dif]
            self.difficulty = new_dif
            new_res = f"{new_dif.screen_width}x{new_dif.screen_height}"
            self.geometry(new_res)
            self.grid_canvas.configure(
                width=self.difficulty.width * 25,
                height=self.difficulty.height * 25,
            )
            self.reset_button.place(x=new_dif.screen_width // 2, y=21, anchor="center")
            #! REMOVE PRINT WHEN DONE
            print(
                f"changed difficulty from {old_dif} to {new_dif.name}. new_res:{new_res}"
            )

        return inner

    def get_difficulty(self) -> GridDifficulty:
        return self.difficulty


class Reset(tk.Button):
    """
    Reset button for restarting the game
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.configure(text="Reset", command=self.reset_board)
        self.parent = parent

    def reset_board(self):
        #! REMOVE PRINT HEN DONE
        print("pressed restet button")


def grid_img_make(filename: str) -> PhotoImage:
    """
    function to load images easier
    """
    if not isinstance(filename, str):
        raise TypeError(
            f"param:filename must be type<str> not type<{type(filename).__name__}>"
        )
    img = ImageTk.PhotoImage(
        Image.open(filename).resize((25, 25), Image.Resampling.LANCZOS)
    )
    return img


#! WORK ON BOMB FINDING ALGO
class GridSquare(tk.Canvas):
    def __init__(self, parent: Window, row_idx: int, col_idx: int, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent: Window = parent

        # grid square images
        self.grid_sqr_unclicked: PhotoImage = grid_img_make("./images/grid_square1.png")
        self.grid_sqr_clicked: PhotoImage = grid_img_make("./images/grid_square2.png")
        self.flag_image: PhotoImage = grid_img_make("./images/grid_flag1.png")

        # grid number images
        self.grid_num_1: PhotoImage = grid_img_make("./images/nums/grid_num_1.png")
        self.grid_num_2: PhotoImage = grid_img_make("./images/nums/grid_num_2.png")
        self.grid_num_3: PhotoImage = grid_img_make("./images/nums/grid_num_3.png")
        self.grid_num_4: PhotoImage = grid_img_make("./images/nums/grid_num_4.png")
        self.grid_num_5: PhotoImage = grid_img_make("./images/nums/grid_num_5.png")
        self.grid_num_6: PhotoImage = grid_img_make("./images/nums/grid_num_6.png")
        self.grid_num_7: PhotoImage = grid_img_make("./images/nums/grid_num_7.png")
        self.grid_num_8: PhotoImage = grid_img_make("./images/nums/grid_num_8.png")

        self.row_idx_loc = row_idx
        self.col_idx_loc = col_idx
        self.max_r_width, self.max_c_height = self.set_grid_ranges()
        self.num_bombs = 0

    def set_grid_ranges(self) -> tuple:
        dif: GridDifficulty = self.parent.get_difficulty()
        return dif.width, dif.height

    def count_bombs(self):
        pass


def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()
