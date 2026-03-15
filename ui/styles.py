# ─── Colours ─────────────────────────────────────────────────────────────────
#   All colour values are standard hex RGB strings accepted by tkinter.

BACKGROUND     = "#2c3e50"   # Dark blue-grey  – main window background
FOREGROUND     = "#ecf0f1"   # Off-white       – general text (title, unit)
ACCENT         = "#1abc9c"   # Teal            – the highlighted value number
BOX_BACKGROUND = "#34495e"   # Slightly lighter – individual number-box background


# ─── Fonts ────────────────────────────────────────────────────────────────────
#   Tkinter font format: (family, size)  or  (family, size, weight)
#   'Segoe UI' is available on Windows; tkinter falls back gracefully elsewhere.

FONT_FAMILY = "Segoe UI"

FONT_TITLE  = (FONT_FAMILY, 13)
FONT_VALUE  = (FONT_FAMILY, 64, "bold")
FONT_UNIT   = (FONT_FAMILY, 13)


# ─── Spacing ──────────────────────────────────────────────────────────────────
#   All values are in pixels.

BOX_OUTER_PADDING = 20   # Space between each number-box and the window edge
BOX_GAP           = 40   # Space between the two number-boxes
BOX_INNER_PADDING = 16   # Space between the box border and its own labels
