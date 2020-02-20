import tkinter as tk
import requests


H = 500  # these are the dimensions for the the canvas of the window.
W = 700


def test(entry):
	print('This is the entry: ',entry)


def get_weather(city):
	weather_key = ' '  # put your API key for accessing your accout on OpenWeatherAPI.
	url = ' '  # put the url link of the API which your app is gonig to use.
	para = {
		'APPID': weather_key,
		'q': city,
		'units': 'Imperial',
	}
	response = requests.get(url, params=para)
	weather = response.json()

	label_below['text'] = format_response(weather)


def format_response(weather):
	name = weather['name']
	desc = weather['weather'][0]['description']
	temp = weather['main']['temp']

	return str(name) + '\n' + str(desc) + '\n' + str(temp)


root = tk.Tk()  # this is the root(initial) window created.

# this is the default canvas for the window(resizable).
canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()  # placing the canvas in the context of the root window.

# this is the basic background for the canvas of the window in the the form of frames.
frame_bg = tk.Frame(root, bg='white')
frame_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

bg_image = tk.PhotoImage(file='images/bg_img.png')
bg_label = tk.Label(frame_bg, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# frame_side = tk.Frame(root, bg='#80c1ff')  # '#80c1ff' is the hexadecimal color value for 'light blue'.
# frame_side.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

frame_center = tk.Frame(root, bg='azure')
frame_center.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)

frame_below = tk.Frame(root, bg='azure')
frame_below.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.4)

label = tk.Label(frame_bg, bg='azure', fg='black', text='Weather Report', font=8)
label.place(relx=0.35, rely=0.08, relwidth=0.3, relheight=0.1)

# this is an text field in the frame_center.
entry = tk.Entry(frame_center, bg='orange', fg='white')
entry.place(relx=0.05, rely=0.25, relwidth=0.6, relheight=0.5)

# this will pass an button to the frame_center in the root window.
button = tk.Button(frame_center, text='Click', bg='green', fg='white', font=5, command=lambda: get_weather(entry.get()))
button.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.5)


# another label for the information purpose.
label_below = tk.Label(frame_below, bg='orange', fg='black', text='Attention\n\nToday the weather \nis as follows.', font=8)
label_below.place(relx=0.03, rely=0.1, relwidth=0.932, relheight=0.8)

# this is to display the name on the side of the window.
# label_side = tk.Label(frame_side, bg='white', text='This app \n\nis Developed By \n\nRushikesh Powar')
# label_side.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.95)

root.mainloop()  # termination of the root window.
