from tkinter import *
from tkinter.ttk import *

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")

        self.master.title("Quit button")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=150, y=50)


def main():
    root = Tk()
    root.geometry("250x250+500+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()