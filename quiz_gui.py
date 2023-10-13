import tkinter as tk
from tkinter import Radiobutton, Toplevel
from PIL import Image, ImageTk

class QuizAppGUI:
    def __init__(self, gui, questions):
        self.gui = gui
        self.questions = questions
        self.current_question = 0
        self.score = 0

        # Set up the main application window
        gui.title("QuizMe - Quiz Game Application")
        self.display_title()

        # Create labels, buttons, and option frames
        self.question_label = tk.Label(gui, text="", font=("Arial", 12))
        self.question_label.grid(row=2, column=0, columnspan=2)

        self.var = tk.StringVar()
        self.var.set(None)

        self.option_frame = tk.Frame(gui)
        self.option_frame.grid(row=3, column=0, columnspan=2, padx=10)

        self.option_labels = []

        for i in range(4):
            self.option_labels.append(Radiobutton(self.option_frame, text="", variable=self.var, value="", font=("Arial", 10)))
            self.option_labels[i].grid(row=i, column=0, padx=10, sticky="w")

        button_width = 15
        button_color = "light sky blue3"

        # Create buttons (Next, Quit, Play Again) and labels
        self.next_button = tk.Button(gui, text="Next", command=self.check_answer, bg=button_color, fg="white", font=("Arial", 12, "bold"), width=button_width)
        self.next_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.quit_button = tk.Button(gui, text="Quit", command=gui.quit, bg=button_color, fg="white", font=("Arial", 12, "bold"), width=button_width)
        self.quit_button.grid(row=1, column=1, sticky="ne", pady=10, padx=60)

        # Create the "Play Again" button
        self.play_again_button = tk.Button(gui, text="Play Again", command=self.restart_quiz, bg=button_color, fg="white", font=("Arial", 12, "bold"), width=button_width)
        self.play_again_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.play_again_button.grid_remove()

        # Display the first question
        self.display_question()

    def display_title(self):
        # Create the title label at the top of the application.
        title = tk.Label(self.gui, text="QuizMe", width=50, bg="dodger blue4", fg="white", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2)

    def display_question(self):
        # Display the current question and answer options.
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question = question_data["question"]
            options = question_data["options"]
            self.question_label.config(text=question)
            for i in range(4):
                if i < len(options):
                    self.option_labels[i].config(text=options[i], value=options[i], state="active")
                else:
                    self.option_labels[i].config(text="", value="", state="disabled")
        else:
            self.show_score()

    def check_answer(self):
        # Check if the user's answer is correct.
        selected_option = self.var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_option == correct_answer:
            self.score += 1
        self.next_question()

    def next_question(self):
        # Move to the next question.
        self.current_question += 1
        self.var.set(None)
        self.display_question()

    def show_score(self):
        # Show the final score and an image based on the percentage.
        self.next_button.config(state="disabled")
        self.play_again_button.grid()
        score_window = Toplevel(self.gui)
        score_window.title("QuizMe - Your Score")
        correct_answers = self.score
        total_questions = len(self.questions)
        percentage = (correct_answers / total_questions) * 100
        score_label = tk.Label(score_window, text=f"Your Score: {correct_answers}/{total_questions} ({percentage:.2f}%)", font=("Arial", 14))
        score_label.pack()

        if percentage >= 70:
            image = Image.open("cute-star.png")
        else:
            image = Image.open("sad-face.jpg")

        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(score_window, image=photo)
        image_label.photo = photo
        image_label.pack()

    def restart_quiz(self):
        # Restart the quiz.
        self.current_question = 0
        self.score = 0
        self.play_again_button.grid_remove()
        self.next_button.config(state="active")
        self.display_question()