import tkinter

main_window = tkinter.Tk()
main_window.title('MyApp')
label1 = tkinter.Label(main_window, text='RED Text', bg='red')
label1.pack(fill=tkinter.Y)
label2 = tkinter.Label(main_window, text='Green Text', bg='green')
label2.pack(fill=tkinter.X)
label5 = tkinter.Label(main_window, text='Magenta Text', bg='magenta')
label5.pack(side=tkinter.BOTTOM, fill=tkinter.X)
label3 = tkinter.Label(main_window, text='BLUE Text', bg='blue')
label3.pack(side=tkinter.LEFT, fill=tkinter.Y)
label4 = tkinter.Label(main_window, text='Yellow Text', bg='yellow')
label4.pack(side=tkinter.RIGHT, fill=tkinter.Y)


main_window.mainloop()