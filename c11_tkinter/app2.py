import tkinter


class LoginWindow:
    username = None
    password = None

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('App 2')

        for count, txt in enumerate(['Username: ', 'Password: ']):
            label = tkinter.Label(self.main_window, text=txt)
            label.grid(row=count, column=0)

        for count, label in enumerate(['username', 'password']):
            self.__setattr__(label, tkinter.Entry(self.main_window))
            self.__getattribute__(label).grid(row=count, column=1)

        for count, txt in enumerate(['Login', 'Cancel']):
            button = tkinter.Button(self.main_window, text=txt, command=self.user_pass if not count else quit)
            button.grid(row=2, column=count, sticky=tkinter.E if not count else tkinter.W)

        self.check = tkinter.IntVar()
        check_box = tkinter.Checkbutton(self.main_window, text="I'm not a robot", variable=self.check)
        check_box.grid(row=3, columnspan=2)

    def user_pass(self):
        usern = 'Username'
        passw = 'Password'
        if self.check.get() == 1:
            if self.username.get() != usern:
                print('username is wrong')
            if self.password.get() != passw:
                print('password is wrong')
        else:
            print('box not checked')

    def run(self):
        self.main_window.mainloop()


login = LoginWindow()
login.run()
