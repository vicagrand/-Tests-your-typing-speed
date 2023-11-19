import tkinter as tk
import random
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text_to_type = self.generate_random_text()
        self.current_index = 0

        self.timer_running = False
        self.start_time = 0

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.root, text="Type the following text:")
        self.instruction_label.pack()

        self.text_display = tk.Text(self.root, height=5, width=50, wrap=tk.WORD)
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.config(state=tk.DISABLED)
        self.text_display.pack()

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def generate_random_text(self):
        # Replace this with a longer text or fetch from an external source
        sample_text = "The quick brown fox jumps over the lazy dog"
        words = sample_text.split()
        random.shuffle(words)
        return " ".join(words)

    def start_typing_test(self):
        if not self.timer_running:
            self.current_index = 0
            self.start_time = time.time()
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.result_label.config(text="")

            self.input_entry.delete(0, tk.END)
            self.input_entry.config(state=tk.NORMAL)
            self.input_entry.focus()

            self.root.bind('<Key>', self.check_typing)

    def check_typing(self, event):
        if self.timer_running:
            current_input = self.input_entry.get()
            if current_input == self.text_to_type[:len(current_input)]:
                if current_input == self.text_to_type:
                    elapsed_time = time.time() - self.start_time
                    self.result_label.config(text=f"Typing speed: {len(self.text_to_type) / (elapsed_time / 60):.2f} WPM")
                    self.timer_running = False
                    self.start_button.config(state=tk.NORMAL)
                    self.input_entry.config(state=tk.DISABLED)
                    self.root.unbind('<Key>')
            else:
                self.result_label.config(text="Incorrect input. Keep typing.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()