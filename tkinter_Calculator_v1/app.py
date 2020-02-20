import tkinter as tk

root = tk.Tk()
root.title('Calculator')


def button_clr():
	entry.delete(0, tk.END)


def button_click(number):
	current_num = entry.get()
	entry.delete(0, tk.END)
	entry.insert(0, str(current_num) + str(number))


def button_sign():
	current_num = entry.get()
	entry.delete(0, tk.END)
	entry.insert(0, "-" + str(current_num))


def button_add():
	first_num = entry.get()
	global f_num
	global math
	math = "add"
	f_num = float(first_num)
	entry.delete(0, tk.END)


def button_sub():
	first_num = entry.get()
	global f_num
	global math
	math = "sub"
	f_num = float(first_num)
	entry.delete(0, tk.END)


def button_mul():
	first_num = entry.get()
	global f_num
	global math
	math = "mul"
	f_num = float(first_num)
	entry.delete(0, tk.END)


def button_div():
	first_num = entry.get()
	global f_num
	global math
	math = "div"
	f_num = float(first_num)
	entry.delete(0, tk.END)


def button_equal():
	second_num = entry.get()
	entry.delete(0, tk.END)

	if math == "add":
		entry.insert(0, f_num + float(second_num))

	if math == "sub":
		entry.insert(0, f_num - float(second_num))

	if math == "mul":
		entry.insert(0, f_num * float(second_num))

	if math == "div":
		entry.insert(0, f_num / float(second_num))


entry = tk.Entry(root, width=25, borderwidth=5, bg='green', fg='white', font=5)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

button_ac = tk.Button(root, text='AC', padx=20, pady=10, bg='red', fg='white', command=button_clr)
button_ac.grid(row=1, column=0, padx=5, pady=10)

button_sign = tk.Button(root, text='( - )', padx=20, pady=10, bg='blue', fg='white', command=button_sign)
button_sign.grid(row=1, column=1, padx=5, pady=10)

button_1 = tk.Button(root, text='1', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(1))
button_1.grid(row=2, column=0, padx=5, pady=10)

button_2 = tk.Button(root, text='2', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(2))
button_2.grid(row=2, column=1, padx=5, pady=10)

button_3 = tk.Button(root, text='3', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(3))
button_3.grid(row=2, column=2, padx=5, pady=10)

button_4 = tk.Button(root, text='4', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(4))
button_4.grid(row=3, column=0, padx=5, pady=10)

button_5 = tk.Button(root, text='5', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(5))
button_5.grid(row=3, column=1, padx=5, pady=10)

button_6 = tk.Button(root, text='6', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(6))
button_6.grid(row=3, column=2, padx=5, pady=10)

button_7 = tk.Button(root, text='7', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(7))
button_7.grid(row=4, column=0, padx=5, pady=10)

button_8 = tk.Button(root, text='8', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(8))
button_8.grid(row=4, column=1, padx=5, pady=10)

button_9 = tk.Button(root, text='9', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(9))
button_9.grid(row=4, column=2, padx=5, pady=10)

button_10 = tk.Button(root, text='0', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click(0))
button_10.grid(row=5, column=0, padx=5, pady=10)

button_00 = tk.Button(root, text='00', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click("00"))
button_00.grid(row=5, column=1, padx=5, pady=10)

button_dot = tk.Button(root, text='.', padx=20, pady=10, bg='green', fg='white', command=lambda: button_click("."))
button_dot.grid(row=5, column=2, padx=5, pady=10)

button_div = tk.Button(root, text='/', padx=20, pady=10, bg='orange', fg='white', command=button_div)
button_div.grid(row=1, column=4, padx=5, pady=10)

button_mul = tk.Button(root, text='*', padx=20, pady=10, bg='orange', fg='white', command=button_mul)
button_mul.grid(row=2, column=4, padx=5, pady=10)

button_min = tk.Button(root, text='-', padx=20, pady=10, bg='orange', fg='white', command=button_sub)
button_min.grid(row=3, column=4, padx=5, pady=10)

button_add = tk.Button(root, text='+', padx=20, pady=10, bg='orange', fg='white', command=button_add)
button_add.grid(row=4, column=4, padx=5, pady=10)

button_equal = tk.Button(root, text='=', padx=20, pady=10, bg='orange', fg='white', command=button_equal)
button_equal.grid(row=5, column=4, padx=5, pady=10)

root.mainloop()
