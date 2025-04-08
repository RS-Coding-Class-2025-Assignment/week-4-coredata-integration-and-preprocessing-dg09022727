import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Assignment 3")
root.geometry("300x200") 


progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)
progress["maximum"] = len(steps)

status_label = tk.Label(root, text="Waiting...")
status_label.pack()

count_label = tk.Label(root, text="Step")
count_label.pack()

def run_steps():
    status_label.config(text=steps[0])
    print(steps[0])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[1])
    print(steps[1])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[2])
    print(steps[2])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[3])
    print(steps[3])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[4])
    print(steps[4])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[5])
    print(steps[5])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[6])
    print(steps[6])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[7])
    print(steps[7])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[8])
    print(steps[8])
    progress.step(1)
    root.update()
    time.sleep(1)

    status_label.config(text=steps[9])
    print(steps[9])
    progress.step(1)
    root.update()
    time.sleep(1)


start_button = tk.Button(root, text="Start", command=run_steps)
start_button.pack(pady=10)

root.mainloop()
