# imports
import tkinter as tk
from ui.components import NumberBox

# main app class
class App:
    def __init__(self):
        # initialize app
        self.root = tk.Tk()
        self.root.title("Boxes and numbers")
        self.root.geometry("800x600")

        # Make the boxes
        self.speedBox = NumberBox(self.root,"Speed",23,2,"mm/s")
        self.rpmBox = NumberBox(self.root,"RPM",123,1,"rpm")

        # Place the boxes
        self.speedBox.grid(row=0,column=0)
        self.rpmBox.grid(row=0,column=1)
    
    def update_loop(self):
        self.root.after(100, self.update_loop)

    def run(self):
        # Start the "heartbeat" the updates the ui at regular intervals
        self.update_loop()
        
        # Start the main event loop of tkinter
        self.root.mainloop()

# main entry point
if __name__ == "__main__":
    # create app instance
    app = App()

    # run app
    app.run()
