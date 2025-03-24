import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 10

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Canvas")

        # Create canvas
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Draw a grid of blue squares
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells.append(cell)

        # Create eraser (a pink square)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

        # Bind mouse movement to erase function
        self.canvas.bind("<Motion>", self.erase_objects)

    def erase_objects(self, event):
        """Move eraser and erase overlapping objects"""
        self.canvas.moveto(self.eraser, event.x, event.y)

        # Find objects overlapping with the eraser
        overlapping_objects = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)

        for obj in overlapping_objects:
            if obj != self.eraser:  # Don't erase the eraser itself
                self.canvas.itemconfig(obj, fill="white")

# Run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
