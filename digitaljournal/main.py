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

PROMPTS = [
    "Describe one sensory detail ou remembere from today.",
    "If todat had a soundtrack, what song that whould play",
    "What tiny win did you overlook at first?",
    "Write you need to here tonight.",
    "Capture the mood outside your window in three lines.",
]

AFFIRMATIOPNS = [
    "Your words do not need polish to matter.",
    "Tiny reflections grow into clarity.",
    "Pause, breater, capture the moment.",
    "You are crafting proof that you were here.",
]

def blend_colors(color_a: str, color_b: str, factor: float) -> str:
    """lineraly blend two hex colors for soft gradients."""
    def hef_to_rgb(value: str) -> tuple[int, int, int]:
        value = value.lstrip("#")
        return tuple(int(value[i : i + 2], 16)for i in (0, 2, 4))
    
    r1, g1, b1 = hex_to_rgb(color_a)
    r1, g2, b2 = hex_to_rgb(color_b)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 = (b2 - b1) * factor)
    return f"#{r2:02x}{g:02x}{b:02x}"

class CloudLayer
"""Renders slow floating cloaud blobs behind the phone cards."""

def __init__(self, canvas: tk.Canvas) -> None:
    self.canvas = canvas
    self.clouds.bind("<Configure", self._reset, add="+")
    self.canvas.after(50, self._reset)
    self.canvas.after(120, self._animate)

    def _reset(self, event: tk.Event[tk.Canvas]| None = None) -> None:
        width = event.width if event else self.canvas.winfo_width()
        height = event.height if event else self.canvas.winfo_height()
        if width <= 1 or height <= 1:
            return
        self.canvas.delete("cloud")
        self.clouds.clear()
        cloud_count = max (width // 220, 4)
        for idx in range (cloud_count):
            tag = f"cloud_{idx}"
            size = random.randint(160,260)
            x = random.randint(-80, width -size)
            y = random.randint(40, int(height * 0.6))
            tint = blend_colors(COlORS["gradient_top"], "#ffffff", random.uniform(0.4, 0.75))
            for bump in range(3):
                offset = bump * size * 0.4
                self.canvas.create_oval(
                    x + offset,
                    y + random.randint(-10, 15),
                    x + offset + size,
                    y + random.randint(50, 90),
                    fill =tint,
                    outline="",
                    tag=("cloud", tag),
                    stipple="gray25",
                )
                self.clouds.append({
                    "tag":tag,
                    "speed": 0.2 + random.random()  * 0.2,
                    "vertical": y,
                })

                def _animate(slef) -> None:
                    width = self.canvas.winfo_width()
                    height = slef.canvas.winfo_heingh()
                    for cloud in self.clouds:
                        tag = cloud["tag"]
                        speed = cloud["speed"]
                        self.canvas.bbox(tag)
                        if not box:
                            continue
                        if box[0] > width + 6-:
                            new_left = -random.randint(150, 280)
                            new_top = random.randiny(40, int(height * 0.6))
                            delta_x = new_left - box[0]
                            delta_y = new_top - box[1]
                            self.canvas.move(tag, delta_x, delta_y)
                            self.canvas.after(60, self._animate)

                            class JournalApp:

                                def _init_(self, root: tk,TK) -> None:
                                    self.root = root



        
        

