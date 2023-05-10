import tkinter


class MainMenu():
    title = 'Main Menu'

    def __init__(self, main_window: tkinter.Tk):
        self.main_window = main_window
        self.main_window.title(self.title)
        self.add_menu()

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)

        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='File', menu=main_l2)
        #
        main_l3 = tkinter.Menu(self.main_window)
        main_l2.add_cascade(label='New', menu=main_l3)
        #
        main_l3.add_command(label='New Project', command=self.new_window)
        main_l3.add_command(label='New Project in same Window', command=quit)

        main_l2.add_separator()

        main_l2.add_command(label='Close', command=quit)

    def new_window(self):
        window = tkinter.Tk()
        new_window = MainMenu(window)
        new_title = self.title + ' Copy'
        new_window.main_window.title(new_title)
        new_window.run()

    def run(self):
        self.main_window.mainloop()


window = tkinter.Tk()
main_menu = MainMenu(window)
main_menu.run()
