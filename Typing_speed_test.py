import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.text_to_type = "The quick brown fox jumps over the lazy dog."
        self.current_text = tk.StringVar()
        self.current_text.set("Start typing the following text:\n\n" + self.text_to_type)

        self.label = tk.Label(master, textvariable=self.current_text, wraplength=400, justify="left")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(master, textvariable=self.result_var)
        self.result_label.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=10)

    def start_typing_test(self):
        self.start_time = time.time()
        self.start_button.config(state="disabled")
        self.entry.delete(0, "end")
        self.master.bind("<Key>", self.check_typing)

    def check_typing(self, event):
        typed_text = self.entry.get()
        if typed_text == self.text_to_type:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int((len(self.text_to_type.split()) / elapsed_time) * 60)
            self.result_var.set(f"Congratulations! You typed the text correctly.\nWords per minute: {words_per_minute}")
            self.start_button.config(state="normal")
            self.master.unbind("<Key>")
        else:
            self.current_text.set("Start typing the following text:\n\n" + self.text_to_type[:len(typed_text)])

# Main program
root = tk.Tk()
typing_speed_test = TypingSpeedTest(root)
root.mainloop()
