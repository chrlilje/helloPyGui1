# imports
import tkinter as tk
import threading
import queue
from ui.components import NumberBox
from ui import styles
import data_io  # this is the module that fetch our data

# main app class
class App:
    def __init__(self):
        # initialize app
        self.root = tk.Tk()
        self.root.title("Boxes and numbers")
        self.root.configure(bg=styles.BACKGROUND)

        # Size the window to 50 % of the screen, then centre it
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        win_w    = screen_w // 2
        win_h    = screen_h // 2
        offset_x = (screen_w - win_w) // 2
        offset_y = (screen_h - win_h) // 2
        self.root.geometry(f"{win_w}x{win_h}+{offset_x}+{offset_y}")

        # Tell tkinter's grid that both columns share the available width equally,
        # and that the single row may grow to fill the window height.
        # weight=1 means: give all available extra space to this column/row.
        # uniform="boxes" forces both columns to always stay the same width,
        # so a wider value in one box cannot steal space from the other.
        self.root.columnconfigure(0, weight=1, uniform="boxes")
        self.root.columnconfigure(1, weight=1, uniform="boxes")
        self.root.rowconfigure(0, weight=1)

        # Create a Queue for thread safe data communication with the serial-thingy
        self.data_queue: queue.Queue = queue.Queue()

        # Make the boxes - User interface
        self.speedBox = NumberBox(self.root, "Speed", 23,  2, "mm/s")
        self.rpmBox   = NumberBox(self.root, "RPM",   123, 1, "rpm")

        # Place the boxes
        # sticky="nsew" makes each box stretch to fill its entire grid cell.
        # The inner edges use BOX_GAP so there is more breathing room between
        # the two boxes than between a box and the window edge.
        outer = styles.BOX_OUTER_PADDING
        gap   = styles.BOX_GAP
        self.speedBox.grid(row=0, column=0, padx=(outer, gap), pady=outer, sticky="nsew")
        self.rpmBox.grid(  row=0, column=1, padx=(gap, outer), pady=outer, sticky="nsew")
    
    def update_loop(self):

        # Drain the queue and display the latest data
        latest_data = None

        while not self.data_queue.empty():
            try:
                # get_nowait means: Get data immediately. If nothing is there, it raises queue.Empty exception
                latest_data = self.data_queue.get_nowait() 
            except queue.Empty:
                # Safe way to handle if the queue was emptied somewhere else for some reason
                break # break from the 'while not self.data_queue.empty()'

        if latest_data is not None:
            # keys match what data_io.py sends into the queue
            if "speed" in latest_data:
                self.speedBox.update_value(latest_data["speed"])
            if "rpm" in latest_data:
                self.rpmBox.update_value(latest_data["rpm"])
        
        # schedule the next run of the check for updates in 100ms
        self.root.after(100, self.update_loop)

    def run(self):
        # Start fetching data in another thread to keep the UI thread responsive
        data_thread = threading.Thread(
            target=data_io.fetch_data,
            args=(self.data_queue,),
            daemon=True
        )
        data_thread.start()

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
