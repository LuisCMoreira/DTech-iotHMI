import tkinter as tk
from tkinter import PhotoImage
from tkinter.colorchooser import askcolor

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
        self.background_image = self.background_image.zoom(window_width // self.background_image.width())
        self.background_image = self.background_image.subsample(window_height // self.background_image.height())

        background_label = tk.Label(master, image=self.background_image, bd=0, highlightthickness=0)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Your GUI components go here
        label = tk.Label(master, text="Full Screen Tkinter App", font=("Helvetica", 24), bg='white', padx=10, pady=10)
        label.pack(pady=20)

        # Create three round buttons at absolute locations
        button1 = self.create_round_button("red", "Button 1", x=100, y=100)
        button1.place(x=300, y=350)

        button2 = self.create_round_button("yellow", "Button 2", x=300, y=100)
        button2.place(x=1100, y=350)

        button3 = self.create_round_button("green", "Button 3", x=500, y=100)
        button3.place(x=650, y=350)

    def create_round_button(self, color, text, x, y):
        button = tk.Canvas(self.master, width=250, height=250, bg="white" ,  bd=0,
                   highlightthickness=0, relief="ridge")
        
        button.create_oval(1, 1, 248, 248, fill=color, outline="", width=2)

        # Create a transparent oval around the button
        #button.create_oval(-1, -1, 250, 250, fill="", outline="", width=2)

        button.create_text(125, 125, text=text, font=("Helvetica", 22), fill="black")
        button.bind('<Button-1>', self.change_color)
        return button

    def change_color(self, event):
        new_color = askcolor(title="Choose Color")[1]
        if new_color:
            event.widget.itemconfig(1, fill=new_color)
            print(new_color)

    def exit_full_screen(self, event):
        self.master.attributes('-fullscreen', False)

if __name__ == '__main__':
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
