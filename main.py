import tkinter as tk
from tkinter import ttk
from convertValutes import *

def validateInput(P):
    if P == "" or P.isdigit(): return True
    else: return False

def baseSearch(event):
    value = event.widget.get()
    if value == '':
        base_combo['values'] = names
    else:
        data = []

        for item in names:
            if value.lower() in item.lower():
                data += [item]
        base_combo['values'] = data

def targetSearch(event):
    value = event.widget.get()
    if value == '':
        target_combo['values'] = names
    else:
        data = []

        for item in names:
            if value.lower() in item.lower():
                data += [item]
        target_combo['values'] = data

def on_convert():
    base = currencies[base_combo.get().split("(")[0].strip()]
    target = currencies[target_combo.get().split("(")[0].strip()]
    amount = int(amount_entry.get())
    result = convert(base, target, amount)
    result_label.config(text=result)

def on_select(event):
    base = base_combo.get()
    target = target_combo.get()
    if base and target:
        convert_button.config(state=tk.NORMAL)
    else:
        convert_button.config(state=tk.DISABLED)

root = tk.Tk()
root.geometry("760x680")
root.title("Converter App by enginex")

# top
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, padx=20, pady=20)

left_frame = tk.Frame(top_frame)
left_frame.pack(side=tk.LEFT, padx=20)

base_label = tk.Label(left_frame, text="Base:")
base_label.pack()

base_combo = ttk.Combobox(left_frame, values=names)
base_combo.pack()
base_combo.bind("<<ComboboxSelected>>", on_select)
base_combo.bind('<KeyRelease>', baseSearch)

base_value_label = tk.Label(left_frame, text="Base: ")
base_value_label.pack()

right_frame = tk.Frame(top_frame)
right_frame.pack(side=tk.RIGHT, padx=20)

target_label = tk.Label(right_frame, text="Target:")
target_label.pack()

target_combo = ttk.Combobox(right_frame, values=names)
target_combo.pack()
target_combo.bind("<<ComboboxSelected>>", on_select)
target_combo.bind('<KeyRelease>', targetSearch)

target_value_label = tk.Label(right_frame, text="Target: ")
target_value_label.pack()

# middle
center_frame = tk.Frame(root)
center_frame.pack(side=tk.TOP, pady=20)

validate_cmd = root.register(validateInput)
amount_entry = tk.Entry(center_frame, validate="key", validatecommand=(validate_cmd, '%P'))
amount_entry.insert(0, "100")
amount_entry.pack()

convert_button = tk.Button(center_frame, text="Convert", state=tk.DISABLED, command=on_convert)
convert_button.pack()

result_label = tk.Label(center_frame, text="")
result_label.pack()

root.mainloop()
