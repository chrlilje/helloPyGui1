# imports
import tkinter as tk
import threading
import queue
from ui.components import NumberBox
import data_io  # this is the module that fetch our data

# main app class
class App:
    def __init__(self):
        # initialize app
        self.root = tk.Tk()
        self.root.title("Boxes and numbers")
        self.root.geometry("800x600")

        # Create a Queue for thread safe data communication with the serial-thingy
        self.data_queue : queue.Queue = queue.Queue()

        # Make the boxes - User interface
        self.speedBox = NumberBox(self.root,"Speed",23,2,"mm/s")
        self.rpmBox = NumberBox(self.root,"RPM",123,1,"rpm")

        # Place the boxes
        self.speedBox.grid(row=0, column=0, padx=20, pady=20)
        self.rpmBox.grid(row=0, column=1 , padx=20, pady=20)
    
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

        if latest_data:
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
