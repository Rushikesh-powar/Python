import tkinter as tk
import turtle

Height = 480
Width = 720

my_turtles = turtle.Turtle()

root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root, bg='light blue')
frame.place(relx=0.02, rely=0.01, relwidth=0.95, relheight=0.9)

lab_1 = tk.Label(frame, text="Length / Radius", bg='orange', fg='white')
lab_1.place(relx=0.03, rely=0.05, relwidth=0.15, relheight=0.08)

lab_2 = tk.Label(frame, text="Breadth / Angle", bg='orange', fg='white')
lab_2.place(relx=0.03, rely=0.15, relwidth=0.15, relheight=0.08)

entry = tk.Entry(frame, width=10, borderwidth=5)
entry.place(relx=0.19, rely=0.05, relwidth=0.2, relheight=0.08)

entry_1 = tk.Entry(frame, width=10, borderwidth=5)
entry_1.place(relx=0.19, rely=0.15, relwidth=0.2, relheight=0.08)


def my_square(move):
	square(my_turtles, move)


def my_circle(radius):
	rounds(my_turtles, radius)


def my_rectangle(lent, bred):
	rectangle(my_turtles, lent, bred)


def my_linear(move):
	line(my_turtles, move)


def my_rotate_left(angle):
	rotate_l(my_turtles, angle)


def my_rotate_right(angle):
	rotate_r(my_turtles, angle)


def rotate_l(my_turtle, angle):
	my_turtle.left(angle)


def rotate_r(my_turtle, angle):
	my_turtle.right(angle)


def line(my_turtle, move):
	my_turtle.pensize(2)
	my_turtle.color('light blue')
	my_turtle.forward(move)


def square(my_turtle, move):
	my_turtle.pensize(2)
	my_turtle.color('gray')

	for i in range(4):
		my_turtle.forward(move)
		my_turtle.right(90)


def rectangle(my_turtle, lent, bred):
	my_turtle.pensize(2)
	my_turtle.color('black')

	for i in range(2):
		my_turtle.forward(lent)
		my_turtle.right(90)
		my_turtle.forward(bred)
		my_turtle.right(90)


def rounds(my_turtle, radius):
	my_turtle.pensize(2)
	my_turtle.color('green')
	my_turtle.circle(radius)


button_square = tk.Button(frame, width=20, height=10, text="Square", bg='green', fg='white', command=lambda: my_square(float(entry.get())))
button_square.place(relx=0.03, rely=0.3, relwidth=0.15, relheight=0.1)

button_circle = tk.Button(frame, width=20, height=10, text="Circle", bg='green', fg='white', command=lambda: my_circle(float(entry.get())))
button_circle.place(relx=0.03, rely=0.42, relwidth=0.15, relheight=0.1)

button_rect = tk.Button(frame, width=20, height=10, text="Rectangle", bg='green', fg='white', command=lambda: my_rectangle(float(entry.get()), float(entry_1.get())))
button_rect.place(relx=0.03, rely=0.54, relwidth=0.15, relheight=0.1)

button_line = tk.Button(frame, width=20, height=10, text="Line", bg='green', fg='white', command=lambda: my_linear(float(entry.get())))
button_line.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.1)

button_rot_L = tk.Button(frame, width=20, height=10, text="Rotate Left", bg='green', fg='white', command=lambda: my_rotate_left(float(entry_1.get())))
button_rot_L.place(relx=0.2, rely=0.42, relwidth=0.15, relheight=0.1)

button_rot_R = tk.Button(frame, width=20, height=10, text="Rotate Right", bg='green', fg='white', command=lambda: my_rotate_right(float(entry_1.get())))
button_rot_R.place(relx=0.2, rely=0.54, relwidth=0.15, relheight=0.1)

root.mainloop()
