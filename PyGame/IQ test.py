import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "Какое число должно быть следующим в ряду: 2, 4, 8, 16?",
        "options": ["32", "24", "20", "18"],
        "answer": "32"
    },
    {
        "question": "Найдите лишнее слово: Кошка, Собака, Ягода, Курица",
        "options": ["Кошка", "Собака", "Ягода", "Курица"],
        "answer": "Ягода"
    },
    {
        "question": "Продолжите последовательность: 1, 1, 2, 3, 5, 8, ?",
        "options": ["10", "12", "13", "21"],
        "answer": "13"
    },
    {
        "question": "Сколько букв в русском алфавите?",
        "options": ["30", "31", "32", "33"],
        "answer": "33"
    },
    {
        "question": "Как называется фигура с 8 сторонами?",
        "options": ["Гексагон", "Гептагон", "Октагон", "Декагон"],
        "answer": "Октагон"
    }
]

class IQTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IQ Test")
        self.score = 0
        self.current_question = 0
        self.setup_ui()

    def setup_ui(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", width=30, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Исправленный отступ
        self.next_button = tk.Button(self.root, text="Следующий вопрос", command=self.next_question)
        self.next_button.pack(pady=20)

        self.display_question()

    # Исправленный уровень отступа для метода display_question
    def display_question(self):
        q = questions[self.current_question]
        self.question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option)

    def check_answer(self, selected_idx):
        selected_option = questions[self.current_question]["options"][selected_idx]
        if selected_option == questions[self.current_question]["answer"]:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(questions):
            self.display_question()
        else:
            iq_score = 80 + self.score * 10
            messagebox.showinfo("Результат", f"Вы ответили правильно на {self.score} из {len(questions)} вопросов.\nВаш IQ: {iq_score}")
            self.root.quit()

root = tk.Tk()
app = IQTestApp(root)
root.mainloop()