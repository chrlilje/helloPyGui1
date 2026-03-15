import tkinter as tk
from . import styles


class NumberBox(tk.Frame):
    """
    A display widget that shows a titled numeric value with a unit.
    Inherits from the tkinder.Frame class
    
    Layout (top to bottom, all centred):
        title  – small label
        value  – large number, grows with the box
        unit   – small label
    """

    def __init__(self, parent: tk.Widget, title: str, value: float = 0,
                 precision: int = 1, unit: str = ""):
        super().__init__(parent, bg=styles.BOX_BACKGROUND)

        # Keep precision so update_value can format correctly
        self.precision = precision

        p = styles.BOX_INNER_PADDING   # shorthand for less repetition below

        # ── Row 0: title ──────────────────────────────────────────────────────
        self.label_title = tk.Label(
            self,
            text=title,
            font=styles.FONT_TITLE,
            bg=styles.BOX_BACKGROUND,
            fg=styles.FOREGROUND,
        )
        self.label_title.grid(
            row=0, column=0, sticky="ew",
            padx=p, pady=(p, 0)
        )

        # ── Row 1: value ──────────────────────────────────────────────────────
        self.label_value = tk.Label(
            self,
            font=styles.FONT_VALUE,
            bg=styles.BOX_BACKGROUND,
            fg=styles.ACCENT,
        )
        self.label_value.grid(
            row=1, column=0, sticky="nsew",
            padx=p
        )

        # ── Row 2: unit ───────────────────────────────────────────────────────
        self.label_unit = tk.Label(
            self,
            text=unit,
            font=styles.FONT_UNIT,
            bg=styles.BOX_BACKGROUND,
            fg=styles.FOREGROUND,
        )
        self.label_unit.grid(
            row=2, column=0, sticky="ew",
            padx=p, pady=(0, p)
        )

        # Let row 1 (the value row) absorb all extra vertical space when the
        # box is resized, so the number stays visually centred between title
        # and unit.
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Render the initial value
        self.update_value(value)

    def update_value(self, new_value: float):
        self.value = new_value
        self.label_value.config(text=f"{self.value:.{self.precision}f}")


class StatusLabel(tk.Frame):
    """
    A simple status line component for short messages.

    Designed to sit under the NumberBox widgets and span both columns.
    """

    def __init__(self, parent: tk.Widget, text: str = ""):
        super().__init__(parent, bg=styles.BACKGROUND)

        self.label = tk.Label(
            self,
            text=text,
            font=styles.FONT_UNIT,
            bg=styles.BACKGROUND,
            fg=styles.FOREGROUND,
            anchor="w",
        )
        self.label.grid(row=0, column=0, sticky="ew")

        self.columnconfigure(0, weight=1)

    def update_text(self, text: str):
        self.label.config(text=text)


