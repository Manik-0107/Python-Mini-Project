import tkinter as tk
from tkinter import messagebox

#---------------QUIZ Data---------------
quiz_data = [
    {
        "question" : "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "correct_answer": "Delhi"
    },
    {
        "question" : "Which language is used for web apps?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "correct_answer": "JavaScript"
    },
    {
        "question" : "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "correct_answer": "Guido van Rossum"
    },
    {
        "question" : "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "correct_answer": "12"
    }
]

#------------APP class--------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quix Game")
        self.root.geometry("500x400")

        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.selected_option = tk.StringVar()

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_option, value="", font=("Arial", 12))
            rb.pack(anchor="w", padx=100)
            self.options.append(rb)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack()

        self.load_question()

    def load_question(self):
        if self.q_index < len(quiz_data):
            q = quiz_data[self.q_index]
            self.question_label.config(text=q["question"])
            self.selected_option.set(None)

            for i, option in enumerate(q["options"]):
                self.options[i].config(text=option, value=option)
        else:
            self.show_result()

    def next_question(self):
        selected = self.selected_option.get()

        if not selected:
            messagebox.showwarning("Warning", "Please select an option")
            return

        correct_answer = quiz_data[self.q_index]["correct_answer"]

        if selected == correct_answer:
            self.score += 1

        self.q_index += 1
        self.score_label.config(text=f"Score: {self.score}")

        self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz completed", f"Your score: {self.score}/{len(quiz_data)}")
        self.root.destroy()

    #--------------------Run APP--------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
