import tkinter as tk
from tkinter import DISABLED, NORMAL, filedialog
from tkinter.scrolledtext import ScrolledText

from main import transpile

size = 900

root = tk.Tk()

code_label = tk.Label(root, text='Source code')
result_label = tk.Label(root, text='Transpiled code')

code_label.place(x=0)
result_label.place(x=size / 2)

code_textarea = ScrolledText(root)
result_textarea = ScrolledText(root)
code_textarea.get("1.0", tk.END)
result_textarea.config(state=DISABLED)
code_textarea.place(width=size / 2, height=size - 40 - 40 - 20, y=20)
result_textarea.place(x=size / 2, width=size / 2, height=size - 40 - 40 - 20, y=20)

error_text = tk.StringVar()
error_text.set('Ready')
error_message = tk.Label(root, text='Ready', fg='#FF0000', textvariable=error_text)
error_message.place(x=80, y=size - 40 - 40)


def on_open_file():
    filename = filedialog.askopenfilename()
    code_textarea.delete(1.0, tk.END)
    code_textarea.insert(tk.END, open(filename, 'r').read())


open_file = tk.Button(root, text='Open file', command=on_open_file)
open_file.place(x=0, y=size - 40 - 40, height=40, width=80)


def move_cursor(line, column):
    position = f"{line}.{column}"
    code_textarea.focus_set()
    code_textarea.mark_set("insert", position)
    code_textarea.see(position)


def on_transpile():
    code = code_textarea.get('1.0', tk.END)
    if len(code.strip()) == 0:
        error_text.set('Please insert source code')
        return
    result, err = transpile(code)

    if err is not None:
        error_text.set(err.message)
        move_cursor(err.line, err.column)
        result = 'Check errors'

    result_textarea.config(state=NORMAL)
    result_textarea.delete(1.0, tk.END)
    result_textarea.insert(tk.END, result)
    result_textarea.config(state=DISABLED)


button = tk.Button(root, text='Transpile!', command=on_transpile)
button.place(y=size - 40, width=size, height=40)

code_textarea.delete(1.0, tk.END)
code_textarea.insert(tk.END, open('main.c', 'r').read())

root.title('Compiler - Mateusz Woźniak - Jakub Błażowski - TKiK')
root.geometry(f'{size}x{size}')
root.resizable(False, False)
root.mainloop()
