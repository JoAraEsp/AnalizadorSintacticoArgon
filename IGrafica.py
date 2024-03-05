import ctypes
import re
import tkinter as tk

from tkinter import scrolledtext, messagebox, Button
from ALexico import lexer
from ASintactico import syntactic_analyzer

# ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = tk.Tk()
root.title("Analizador ARGON")
root.geometry("800x600")


def analyze_lexicon():
    code = editArea.get("1.0", tk.END)
    print(code)

    tokens = lexer(code)

    results_win = tk.Toplevel(root)
    results_win.title("Resultados del Análisis Léxico")

    result_text = scrolledtext.ScrolledText(results_win, width=80, height=40)
    result_text.pack()

    seen_types = set()

    for token in tokens:
        type, value = token
        if type not in seen_types:
            valores = ",".join([v for t, v in tokens if t == type])
            result_text.insert(tk.END, "{}: {}\n".format(type, valores))
            seen_types.add(type)


def analyze_syntax():
    code = editArea.get("1.0", tk.END)

    response = syntactic_analyzer(code)

    if response['status'] == 'success':
        messagebox.showinfo("Syntax Analysis", response['message'])
    else:
        messagebox.showerror("Syntax Analysis", response['message'])



def changes(event=None):
    global previousText

    if editArea.get("1.0", tk.END) == previousText:
        return

    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")

    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get("1.0", tk.END)):
            editArea.tag_add(f"{i}", start, end)
            editArea.tag_config(f"{i}", foreground=color)

            i += 1

    previousText = editArea.get("1.0", tk.END)


def search_re(pattern, text, groupid=0):
    matches = []

    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):
            matches.append((f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}"))

    return matches


def rgb(rgb):
    return "#%02x%02x%02x" % rgb


previousText = ""
background_color = rgb((255, 255, 255))
normal_color = rgb((0,0,0))
keywords_color = rgb((0,0,0))
function_color = rgb((0,0,0))
string_color = rgb((0,0,0))
comments_color = rgb((0,0,0))
args_color = rgb((0,0,0))
parenthesis_color = rgb((0,0,0))
brace_color = rgb((0,0,0))
symbol_color = rgb((0,0,0))


repl = [
    (r"\bFn\b", function_color),
    (r"\bassuming\b", keywords_color),
    (r"\bloop\b", keywords_color),
    (r"\btrue\b", keywords_color),
    (r"\bfalse\b", keywords_color),
    (r"\botherwise\b", keywords_color),
    (r"\".*?\"", string_color),
    (r"\(", parenthesis_color),
    (r"\)", parenthesis_color),
    (r"\{", brace_color),
    (r"\}", brace_color),
    (r"\=\=", symbol_color),
    (r"\=\>", symbol_color),
    (r"\<\=", symbol_color),
    (r"\!\=", symbol_color),
    (r"\>", symbol_color),
    (r"\<", symbol_color),
    (r"\=", symbol_color),  
    (r"\+\+", symbol_color),
    (r"\-\-", symbol_color),
    (r"\+", symbol_color),
    (r"\-", symbol_color),
    (r"\*", symbol_color),
    (r"\&", symbol_color),
    (r"\:", symbol_color),
]


editArea = scrolledtext.ScrolledText(
    root,
    background=background_color,
    foreground=normal_color,
    insertbackground=normal_color,
    relief=tk.FLAT,
    borderwidth=30,
    font="Consolas 15",
)

editArea.pack(fill=tk.BOTH, expand=1)

editArea.bind("<KeyRelease>", changes)

lexButton = Button (text="Léxico", font=("Arial", 10), bg='white', fg='black', command=analyze_lexicon)
syntaxButton = Button(text="Sintáctico", font=("Arial", 10), bg='white', fg='black', command=analyze_syntax)
lexButton.place(x=280, y=530, width=100, height=30)
syntaxButton.place(x=400, y=530, width=100, height=30)

root.mainloop()

def load_content_from_file(path: str):
    with open(path, 'r') as f:
        return f.read()