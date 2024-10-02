import customtkinter



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("300x400")

# Font for buttons
buttonFont =customtkinter.CTkFont(size=28)


button0 = customtkinter.CTkButton(master=root, text="X", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button0.configure(height = 100, width=100)
button0.grid(row = 0, column = 0)

button1 = customtkinter.CTkButton(master=root, text="○", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button1.configure(height = 100, width=100)
button1.grid(row = 0, column = 1)

button2 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button2.configure(height = 100, width=100)
button2.grid(row = 0, column = 2)

button3 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button3.configure(height = 100, width=100)
button3.grid(row = 1, column = 0)

button4 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button4.configure(height = 100, width=100)
button4.grid(row = 1, column = 1)

button5 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button5.configure(height = 100, width=100)
button5.grid(row = 1, column = 2)

button6 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button6.configure(height = 100, width=100)
button6.grid(row = 2, column = 0)

button7 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button7.configure(height = 100, width=100)
button7.grid(row = 2, column = 1)

button8 = customtkinter.CTkButton(master=root, text="", font=buttonFont, border_width=1, border_color="black", corner_radius=0)
button8.configure(height = 100, width=100)
button8.grid(row = 2 ,column = 2)


root.mainloop()