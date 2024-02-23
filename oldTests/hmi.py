import tkinter as tk
from tkinter import PhotoImage
from tkinter.colorchooser import askcolor

import csvLog as Log
import jsonRead as jRead

class FullScreenApp:
    def __init__(self, master, **kwargs):
        self.master = master
        self.master.title("Full Screen App")
        self.master.bind('<Escape>', self.exit_full_screen)
        self.master.attributes('-fullscreen', True)

        # Load the background image and get the window size
        self.background_image = PhotoImage(file='./images/name.PNG')
        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()

        # Resize the background image to fit the window
        resize_factor_width = window_width // self.background_image.width()
        resize_factor_height = window_height // self.background_image.height()
        self.background_image = self.background_image.zoom(resize_factor_width)
        self.background_image = self.background_image.subsample(resize_factor_height)

        background_label = tk.Label(master, image=self.background_image, bd=0, highlightthickness=0)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load the image buttons
        self.image1 = tk.PhotoImage(file='./images/name1.PNG')
        self.image2 = tk.PhotoImage(file='./images/name2.PNG')
        self.image3 = tk.PhotoImage(file='./images/name3.PNG')


        # Your GUI components go here
        label = tk.Label(master, text="Full Screen Tkinter App", font=("Helvetica", 24), bg='white', padx=10, pady=10)
        label.pack(pady=20)

        # Create three round buttons at absolute locations
        button1 = self.create_round_button("", "Button 1", x=300, y=350)
        button1.place(x=300, y=350)

        button2 = self.create_round_button("", "Button 2", x=650, y=350)
        button2.place(x=650, y=350)

        button3 = self.create_round_button("", "Button 3", x=1100, y=350)
        button3.place(x=1100, y=350)

        # Create three image buttons
        self.button1 = tk.Button(master, image=self.image1, bd=0, highlightthickness=0, command=lambda: self.on_image_click(1))
        self.button1.place(x=300, y=350)

        self.button2 = tk.Button(master, image=self.image2, bd=0, highlightthickness=0, command=lambda: self.on_image_click(2))
        self.button2.place(x=650, y=350)

        self.button3 = tk.Button(master, image=self.image3, bd=0, highlightthickness=0, command=lambda: self.on_image_click(3))
        self.button3.place(x=1100, y=350)

    def create_round_button(self, color, text, x, y):
        button = tk.Canvas(self.master, width=250, height=250, bg="white", bd=0, highlightthickness=0, relief="ridge")
        button.create_oval(1, 1, 248, 248, fill=color, outline="", width=2)

        # Create a transparent oval around the button
        button.create_oval(-1, -1, 250, 250, fill="", outline="", width=2)

        button.create_text(125, 125, text=text, font=("Helvetica", 22), fill="white")
        button.bind('<Button-1>', self.change_color)
        return button

    def change_color(self, event):
        new_color = askcolor(title="Choose Color")[1]
        if new_color:
            event.widget.itemconfig(1, fill=new_color)
            print(new_color)

    def on_image_click(self, button_number):
        # Implement the functionality for image button clicks here
        print(f"Image button {button_number} clicked")
        Log.mainLog(jRead.getFromConfig("message.text"), f"pressed number {button_number}")


    def exit_full_screen(self, event):
        self.master.attributes('-fullscreen', False)

if __name__ == '__main__':
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
