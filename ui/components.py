import tkinter as tk
from . import styles

class NumberBox(tk.Frame):
    def __init__(self, parent:tk.Widget, title:str,value:float=0,precision:int = 1, unit:str = ""):
        super().__init__(parent)
        self.title = title
        self.value = value
        self.precision = precision
        self.unit = unit

        # Title of the box. implement layout later
        self.label_title = tk.Label(
            self,text=self.title,
        )

        # value of the number - use update_value to format value correctly
        self.label_value = tk.Label(
            self,
        )
        self.update_value(self.value)

        # Place content right
        self.label_title.pack()
        self.label_value.pack()
        

    def update_value(self,new_value:float):
        self.value = new_value
        formatted = f"{self.value:.{self.precision}f}"
        self.label_value.config(text=formatted)


