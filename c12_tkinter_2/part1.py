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

from tkinter import ttk


# import tkinter
#
#
# class LoginWindow(tkinter.Frame):
#     username = None
#     password = None
#
#     def __init__(self, main_window, name):
#         super().__init__(main_window)
#         self.main_window = main_window
#         self.main_window.title('App' + name)
#
#         for count, txt in enumerate(['Username: ', 'Password: ']):
#             label = tkinter.Label(self.main_window, text=txt)
#             label.grid(row=count, column=0)
#
#         for count, label in enumerate(['username', 'password']):
#             self.__setattr__(label, tkinter.Entry(self.main_window))
#             self.__getattribute__(label).grid(row=count, column=1)
#
#         for count, txt in enumerate(['Login', 'Cancel']):
#             button = tkinter.Button(self.main_window, text=txt, command=self.user_pass if not count else quit)
#             button.grid(row=2, column=count, sticky=tkinter.E if not count else tkinter.W)
#
#         self.check = tkinter.IntVar()
#         check_box = tkinter.Checkbutton(self.main_window, text="I'm not a robot", variable=self.check)
#         check_box.grid(row=3, columnspan=2)
#
#     def user_pass(self):
#         usern = 'Username'
#         passw = 'Password'
#         if self.check.get() == 1:
#             if self.username.get() != usern:
#                 print('username is wrong')
#             if self.password.get() != passw:
#                 print('password is wrong')
#         else:
#             print('box not checked')
#
#
# # main_window = tkinter.Tk()
# # login1 = LoginWindow(main_window, 'name1')
# # login2 = LoginWindow(main_window, 'name2')
#
#
# main_window = tkinter.Tk()
# f1 = tkinter.Frame(main_window)
# f1.pack()
# f2 = tkinter.Frame(main_window)
# f2.pack()
# main_window.mainloop()