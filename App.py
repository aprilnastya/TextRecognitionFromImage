import pytesseract
import tkinter
from tkinter.filedialog import askopenfilename
from PIL import Image


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Распознавание картинки")

        self.main_frame = tkinter.Frame(master=self, bg="white")
        self.label = tkinter.Label(master=self)
        self.button = tkinter.Button(master=self.main_frame, command=askopenfilename)
        self.button.grid(column=0, row=0)
        self.main_frame.grid()
        self.label.grid(column=0, row=1)

    def recognize(self):
        text = pytesseract.image_to_string(Image.open())


if __name__ == "__main__":
    app = Application()
    app.mainloop()
