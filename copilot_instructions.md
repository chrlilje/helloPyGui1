# Project Architecture & Design Philosophy: "Danish Engineering"

When generating code for this project, adhere strictly to the following architectural patterns. The goal is a "Project Skeleton" that is educational, robust, and maintains a strict separation of concerns.

## 1. Core Architecture (The Bridge Pattern)
* **Class `App`**: The main entry point. It handles UI initialization (Tkinter), coordinates thread lifecycles, and manages the main event loop.
* **The "Chef/Waiter" Pattern**: Always separate data acquisition from data display.
    * **The Chef (Data Thread)**: A background thread (`threading.Thread`) that fetches data (Serial, API, or Mock) and puts it into a queue.
    * **The Waiter (UI Thread)**: A recursive loop in the `App` class (`update_loop`) that drains the queue and updates UI components using `root.after()`.

## 2. Thread Safety & Data Flow
* **`data_queue: queue.Queue`**: Use a thread-safe `queue.Queue` for all communication between background threads and the UI.
* **The "Drain the Pipe" Strategy**: Inside the UI `update_loop`, use a `while not self.data_queue.empty():` loop to "flush" the buffer. 
* **Exception Handling**: Wrap `get_nowait()` in a `try/except queue.Empty` block to handle race conditions gracefully.
* **Data Logic**:
    * For **State** (e.g., Speed, RPM): Keep only the `latest_data` (overwrite).
    * For **Events** (e.g., Encoder Ticks, Steps): Accumulate/Sum all values found in the queue during the flush.

## 3. Folder Structure & Separation
Maintain a clean file structure to allow parallel development:
* `/app.py`: Contains the `App` class, the `update_loop`, and thread ignition.
* `/data_io.py`: Contains the `fetch_data` entry point. It must include a `USE_MOCK` toggle.
* `/model.py`: (When applicable) Contains the "Source of Truth" and business logic.
* `/ui/components.py`: Contains reusable UI classes (e.g., `NumberBox`) that encapsulate their own styling.

## 4. Coding Standards
* **Type Hinting**: All function signatures must include type hints (e.g., `data_queue: Queue`, `value: float`).
* **Explicit Dependency Injection**: Pass the `data_queue` into the data fetching functions as an argument; avoid globals.
* **Clean Exit**: Always set background threads to `daemon=True` so they close when the main window is closed.

## 5. UI Implementation
* **Component-Based**: UI elements should be classes with an `update_value()` method.
* **Non-Blocking**: Never use `time.sleep()` in the UI thread. Use `root.after()` for timing.
* **Layout**: Favor `grid()` for complex dashboards to ensure alignment and scalability.