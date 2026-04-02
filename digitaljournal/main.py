from __future__ import annotations

import os
import random
import subprocess
import sys
import textwrap
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import font as tkfont, messagebox, ttk

APP_TITLE = "Journal"
ENTRY_DIR = Path(__file__).parent / "entries"
DATE_FORMAT = "%Y-%m-%d"

COlORS = {
    "gradient_top": "#d7e8ff",
    "gradient_bottom": "#f4f2ff",
    "left_bg": "#0d101f",
    "left_muted": "#9fa7c9",
    "right_bg": "#e9f5f2",
    "right_muted": "#fdfefe",
    "accent": "#6c63ff",
    "accent_soft": "#cdd7ff",
    "text_dark": "#566171",
    "warning": "#f97316",
}

CARD_COLORS = ["#fcb89a", "#ffe6a7", "#c9e1ff", "#ffd8eb"]
