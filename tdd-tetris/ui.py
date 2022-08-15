import tkinter
from turtle import width
from tkinter import Canvas


class MainUI:

    def __init__(self):
        self.window = self.__init_window()
        self.c_width = 600
        self.c_height = 800
        self.b_length = 25
        self.edge = 30
        self.canvas = Canvas(
            master = self.window, 
            width = self.c_width,
            height = self.c_height,
            relief="solid", bd=2)

        self.btn_start = self.__create_btn("start", self.press_btn_start)

        self.location = 0
        self.__test_draw()
        
        
        #canvas.pack()

    def press_btn_start(self):
        print("start")

    def __init_window(self, title="Tetris", width=600, height=800, sx=100, sy=100):
        window = tkinter.Tk()
        window.title(title)
        window.geometry(f"{width}x{height}+{sx}+{sy}")
        window.resizable(False, False)

        return window

    def __test_draw(self):
        #line=self.canvas.create_line(10,10,20,20,20,130,30,140,fill='red')
        self.canvas.create_rectangle(
            0,0,self.c_width,self.c_height, fill='white')

        x = 100
        y = 10 + self.location
        self.canvas.create_rectangle(
            x,y,x+self.b_length,y+self.b_length,
             fill='red')
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

    def progress(self):
        import time
        while True:
            time.sleep(0.5)
            self.location += self.b_length
            self.__test_draw()

    def start(self):
        import threading
        progress_thread = threading.Thread(target=self.progress)
        progress_thread.start()
        self.window.mainloop()

if __name__ == "__main__":
    main_ui = MainUI()
    main_ui.start()
    

