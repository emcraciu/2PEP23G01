import tkinter


def print_something():
    print('message')


main_window = tkinter.Tk()
main_window.title('MyApp')

button1 = tkinter.Button(main_window, text="test", command=print_something)
button1.grid(row=0, column=0)
text = tkinter.Text(main_window, width=20)
text.grid(row=0, column=1)

entry = tkinter.Entry(main_window, takefocus=True)
entry.grid(row=0, column=2)

main_window.mainloop()
