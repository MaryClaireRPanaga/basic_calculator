import tkinter as tk
from tkinter import messagebox
class ProCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern Pro Calculator")
        self.geometry("360x520")
        self.config(bg="black")
        self.resizable(False, False)
        self.color_background = "black"
        self.color_button_main = "#FA8072"
        self.color_screen_accent = "#1a1a1a"
        self.current_input_value = ""
        self.equation_text_variable = tk.StringVar()
        self.initialize_user_interface()
    def initialize_user_interface(self):
        display_entry = tk.Entry(self, textvariable=self.equation_text_variable, font=('Arial', 32, 'bold'), bg=self.color_screen_accent, fg=self.color_button_main, borderwidth=0, justify="right")
        display_entry.pack(fill="both", padx=10, pady=20, ipady=15)
        button_container_frame = tk.Frame(self, bg=self.color_background)
        button_container_frame.pack(expand=True, fill="both", padx=10, pady=10)
        calculator_buttons = ['(', ')', '%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', 'C', '0', '.', '=']
        current_row, current_column = 0, 0
        for button_text in calculator_buttons:
            if button_text == "=":
                button_command = self.calculate_final_result
            elif button_text == "C":
                button_command = self.clear_input_screen
            else:
                button_command = lambda value=button_text: self.append_to_expression(value)
            action_button = tk.Button(button_container_frame, text=button_text, font=('Arial', 14, 'bold'), bg=self.color_button_main, fg="black", relief="flat", activebackground="white", command=button_command)
            action_button.grid(row=current_row, column=current_column, padx=4, pady=4, sticky="nsew")
            current_column += 1
            if current_column > 3:
                current_column = 0
                current_row += 1
        for i in range(4):
            button_container_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_container_frame.grid_rowconfigure(i, weight=1)
    def append_to_expression(self, input_character):
        self.current_input_value += str(input_character)
        self.equation_text_variable.set(self.current_input_value)
    def clear_input_screen(self):
        self.current_input_value = ""
        self.equation_text_variable.set("")
    def calculate_final_result(self):
        try:
            calculated_result = eval(self.current_input_value)
            self.equation_text_variable.set(calculated_result)
            self.current_input_value = str(calculated_result)
            self.ask_user_for_retry()
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero!")
            self.clear_input_screen()
        except Exception:
            messagebox.showerror("Error", "Invalid mathematical expression!")
            self.clear_input_screen()
    def ask_user_for_retry(self):
        user_wants_to_continue = messagebox.askyesno("Calculator", "Would you like to try again?")
        if user_wants_to_continue:
            self.clear_input_screen()
        else:
            messagebox.showinfo("Exit", "Thank you!")
            self.destroy()