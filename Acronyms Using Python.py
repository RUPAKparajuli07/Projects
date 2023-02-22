import tkinter as tk
import random

class FirstLetterCapitalizer:
    def __init__(self, master):
        self.master = master
        master.title("First Letter Capitalizer")
        master.configure(background='#E6E6E6')

        self.label = tk.Label(master, text="Enter a phrase:", bg='#E6E6E6', fg='#333333', font=('Arial', 14))
        self.label.pack(pady=(10, 0))

        self.entry_bg = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        self.entry = tk.Entry(master, bg=self.entry_bg, font=('Arial', 14))
        self.entry.pack(ipadx=10, ipady=5, padx=20, pady=(0, 10), fill=tk.BOTH, expand=True)

        self.result_fg = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        self.result_label = tk.Label(master, text="", bg='#E6E6E6', fg=self.result_fg, font=('Arial', 14, 'bold'))
        self.result_label.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        self.submit_bg = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        self.submit_button = tk.Button(master, text="Submit", bg=self.submit_bg, fg='#FFFFFF', font=('Arial', 14), command=self.process_input)
        self.submit_button.pack(pady=(0, 10), padx=20, fill=tk.BOTH, expand=True)

        self.quit_button = tk.Button(master, text="Quit", bg='#FF5252', fg='#FFFFFF', font=('Arial', 14), command=master.quit)
        self.quit_button.pack(pady=(0, 10), padx=20, fill=tk.BOTH, expand=True)

        # Configure weight to make the root window and all of its children expandable
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        for i in range(1, 5):
            master.rowconfigure(i, weight=0)
            master.columnconfigure(i, weight=1)

    def process_input(self):
        input_string = self.entry.get()

        if not input_string:
            self.result_label.config(text="Please enter a phrase.", fg=self.result_fg)
            return

        capitalized_words = []
        for sentence in input_string.split("."):
            sentence = sentence.strip()
            if sentence:
                sentence = sentence[0].upper() + sentence[1:]
                capitalized_words.append(sentence)

        result = ". ".join(capitalized_words)
        self.result_label.config(text=result, fg=self.result_fg)


root = tk.Tk()
app = FirstLetterCapitalizer(root)
root.mainloop()
