import tkinter as tk
import json
from quiz_gui import QuizAppGUI

if __name__ == "__main__":
    gui = tk.Tk()
    gui.geometry("800x600")

    # read questions from JSON file
    with open("questions.json", "r") as file:
        questions = json.load(file)

    app = QuizAppGUI(gui, questions)
    gui.mainloop()