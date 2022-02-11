import tkinter
from turtle import width


class MainUI:

    def press_btn_start(self):
        print("start")

    def __init_window(self, title="Tetris", width=600, height=800, sx=100, sy=100):
        window = tkinter.Tk()
        window.title(title)
        window.geometry(f"{width}x{height}+{sx}+{sy}")
        window.resizable(False, False)

        return window

    def __test_draw(self):
        line=self.canvas.create_line(10,10,20,20,20,130,30,140,fill='red')
        self.canvas.pack()

    def __create_btn(self, text, command):
        button = tkinter.Button(self.window,
                text = text,
                overrelief="solid",
                width = 15,
                command=command,
                repeatdelay=1000,
                repeatinterval=100
            )
        button.pack()

        return button

    def __init__(self):
        self.window = self.__init_window()
        self.canvas = tkinter.Canvas(self.window, relief="solid", bd=2)

        self.btn_start = self.__create_btn("start", self.press_btn_start)

        self.__test_draw()
            

        #canvas.pack()

    def show(self):        
        self.window.mainloop()

if __name__ == "__main__":
    main_ui = MainUI()
    main_ui.show()
    

