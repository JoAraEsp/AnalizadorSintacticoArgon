import ctypes
import re
import tkinter as tk

from tkinter import scrolledtext, messagebox
from ALexico import lexer
from ASintactico import syntactic_analyzer

root = tk.Tk()
root.title("Analizador ARGON")
root.geometry("800x600")

