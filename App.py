import pytesseract
import tkinter
from tkinter.filedialog import askopenfilename
from PIL import Image


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Распознавание картинки")

        self.main_frame = tkinter.Frame(master=self, bg="white")
        self.button = tkinter.Button(master=self.main_frame, text="Загрузить картинку", command=self.open_file)
        self.main_frame.grid(column=0, row=0, sticky="WESN")
        self.button.grid(column=0, row=0, sticky="WESN")
        # self.button.config(height=3, width=20)
        self.entry = tkinter.Entry(master=self.main_frame, justify=tkinter.CENTER)
        self.entry.grid(column=1, row=0)
        self.button_recognize = tkinter.Button(master=self.main_frame, text="Распознать текст", command=self.recognize)
        self.button_recognize.grid(column=0, row=1, columnspan=2)
        self.text = tkinter.Text(master=self.main_frame)
        self.text.grid(column=0, row=2, columnspan=2, sticky="WESN")
    

    def open_file(self):
        file_path = askopenfilename()
        if file_path:

            self.entry.delete(0, tkinter.END)
            self.entry.insert(0, file_path)

    def recognize(self):
        file_path = self.entry.get()
        text = pytesseract.image_to_string(Image.open(file_path))
        self.text.delete("0.0", tkinter.END)
        self.text.insert("0.0", text)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
