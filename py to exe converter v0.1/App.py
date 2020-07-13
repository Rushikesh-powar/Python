from tkinter.filedialog import *
from tkinter.messagebox import *
from subprocess import *
from tkinter import *
import os

W, H = (720, 720)


class Application:
	def __init__(self):
		self.root = Tk()
		self.root.title("Exe Converter")

		self.var_1 = BooleanVar()
		self.var_2 = BooleanVar()
		self.var_3 = BooleanVar()

		self.canvas = Canvas(self.root, width=W, height=H).pack()

		self.main_frame = Frame(self.root, background="gray")
		self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.dir_label = Label(self.main_frame, bg="gray", text='Choose Directory :', font=("monospace", 16))
		self.file_label = Label(self.main_frame, bg="gray", text='Choose File          :', font=("monospace", 16), )
		self.hid_imp_label = Label(self.main_frame, bg="gray", text='Hidden Imports:', font=("monospace", 16), state=DISABLED)

		self.one_file_label = Label(self.main_frame, bg='orange', fg='white', text='This will build and compile your'
		' script \nand required libraries into one .exe file', font=("Helvetica", 12, "bold"), justify='left')

		self.window_info_label = Label(self.main_frame, bg='orange', fg='white', text='If your script contains any'
		' \ninteractive GUI than tick this box.', font=("Helvetica", 12, "bold"), justify='left')

		self.hid_info_label = Label(self.main_frame, bg='orange', fg='white', text='if your script could not be compiled'
		' try this\noption with the missing pkg in the text box.', font=("Helvetica", 12, "bold"), justify='left')


		self.dir_entry = Entry(self.main_frame, bd=0, width=30, font=("monospace", 12, 'bold'))
		self.file_entry = Entry(self.main_frame, bd=0, width=30, font=("monospace", 12, 'bold'))
		self.hid_imp_entry = Entry(self.main_frame, bd=0, width=30, font=("monospace", 12, 'bold'), state=DISABLED)

		self.dir_button = Button(self.main_frame, text="Open Directory", fg='green', bg='white', font=("monospace", 12),
		command=lambda: self.openDirectory())
		self.file_button = Button(self.main_frame, text="Open File", fg='green', bg='white', font=("monospace", 12),
		command=lambda: self.openFilePath())
		self.set_button = Button(self.main_frame, text="Check Values", fg='green', bg='white', font=("monospace", 12),
		command=lambda: self.checkButtonState())
		self.convert_btn = Button(self.root, text="Convert", fg='white', bg='green', font=("monospace", 12),
		command=lambda: self.convertToExe())

		self.one_file_cb = Checkbutton(self.main_frame, text='--onefile          ', fg='white', bg='orange', font=("monospace", 16)
		, offvalue=False, onvalue=True, activebackground='gray', activeforeground='white', selectcolor="green", variable=self.var_1)

		self.gui_app_cb = Checkbutton(self.main_frame, text='  -w   (For GUI)', fg='white', bg='orange', font=("monospace", 16),
		offvalue=False, onvalue=True, activebackground='gray', activeforeground='white', selectcolor="green", variable=self.var_2)

		self.hid_imp_cb = Checkbutton(self.main_frame, text='Hidden Imports', fg='white', bg='orange', font=("monospace", 16),
		offvalue=False, onvalue=True, activebackground='gray', activeforeground='white', selectcolor="green", variable=self.var_3)

		self.output_txt = Text(self.main_frame, fg='green', bg='white', wrap=WORD)

		self.dir_label.place(relx=0.02, rely=0.05, relwidth=0.25, relheight=0.03)
		self.file_label.place(relx=0.02, rely=0.15, relwidth=0.25, relheight=0.03)

		self.dir_entry.place(relx=0.28, rely=0.049, relwidth=0.5, relheight=0.04)
		self.file_entry.place(relx=0.28, rely=0.149, relwidth=0.5, relheight=0.04)

		self.dir_button.place(relx=0.8, rely=0.049, relwidth=0.18, relheight=0.04)
		self.file_button.place(relx=0.8, rely=0.149, relwidth=0.18, relheight=0.04)

		self.one_file_cb.place(relx=0.02, rely=0.25, relwidth=0.24, relheight=0.04)
		self.gui_app_cb.place(relx=0.02, rely=0.35, relwidth=0.24, relheight=0.04)
		self.hid_imp_cb.place(relx=0.02, rely=0.45, relwidth=0.24, relheight=0.04)
		self.one_file_label.place(relx=0.33, rely=0.25, relwidth=0.54, relheight=0.06)
		self.window_info_label.place(relx=0.33, rely=0.35, relwidth=0.5, relheight=0.06)
		self.hid_info_label.place(relx=0.33, rely=0.45, relwidth=0.59, relheight=0.06)

		self.hid_imp_label.place(relx=0.02, rely=0.55, relwidth=0.2, relheight=0.03)
		self.hid_imp_entry.place(relx=0.25, rely=0.55, relwidth=0.28, relheight=0.03)
		self.set_button.place(relx=0.55, rely=0.55, relwidth=0.18, relheight=0.04)
		self.convert_btn.place(relx=0.84, rely=0.93, relwidth=0.15, relheight=0.05)

		self.output_txt.place(relx=0.025, rely=0.63, relwidth=0.8, relheight=0.35)

		self.root.update()
		mainloop()

	def checkButtonState(self):
		if self.var_3.get():
			self.hid_imp_label.config(state=NORMAL)
			self.hid_imp_entry.config(state=NORMAL)

		elif self.dir_entry.get() and self.file_entry.get():
			self.convert_btn.config(state=NORMAL)

		else:
			self.hid_imp_label.config(state=DISABLED)
			self.hid_imp_entry.config(state=DISABLED)

	def openDirectory(self):
		path = askdirectory()
		if path:
			self.dir_entry.insert(0, path)
			self.convert_btn.config(state=NORMAL)
		else:
			self.convert_btn.config(state=DISABLED)
			showerror("No Path", "Directory was not selected \neither reselect the Directory or enter manually.")

	def openFilePath(self):
		file_path = askopenfilename()
		if file_path:
			path, file_path = os.path.split(file_path)
			self.file_entry.insert(0, file_path)
			self.convert_btn.config(state=NORMAL)
		else:
			self.convert_btn.config(state=DISABLED)
			showerror("No File", "File was not selected \neither reselect the file or enter name manually.")


	def convertToExe(self):
		path = self.dir_entry.get()
		file_name = self.file_entry.get()
		if path and file_name:
			hid_imp = self.hid_imp_entry.get()
			one_file = self.var_1.get()
			win_gui = self.var_2.get()

			self.Converter(path, file_name, hid_imp, one_file, win_gui)

			self.dir_entry.delete(0, 'end')
			self.file_entry.delete(0, 'end')
			self.hid_imp_entry.delete(0, 'end')
		else:
			showerror("Path Missing !", "Please choose the correct path for Directory and File")
			self.convert_btn.config(state=DISABLED)

	def Converter(self, path, file_name, hid_imp, one_file, win_gui):
		if hid_imp and one_file:
			cmd = [f'{path}', f"pyinstaller --hidden-import={hid_imp} --onefile {file_name}"]
		elif hid_imp and win_gui:
			cmd = [f'{path}', f"pyinstaller --hidden-import={hid_imp} -w {file_name}"]
		elif one_file and win_gui:
			cmd = [f'{path}', f"pyinstaller --onefile -w {file_name}"]
		elif hid_imp:
			cmd = [f'{path}', f"pyinstaller --hidden-import={hid_imp} {file_name}"]
		elif one_file:
			cmd = [f'{path}', f"pyinstaller --onefile {file_name}"]
		elif win_gui:
			cmd = [f'{path}', f"pyinstaller -w {file_name}"]
		else:
			cmd = [f'{path}', f"pyinstaller {file_name}"]

		try:
			process = Popen(cmd[1], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=cmd[0], universal_newlines=True)

			a = []
			a.append(process.stderr.read().splitlines())
			n=0
			for lines in a:
				for line in lines:
					self.output_txt.insert(float(n), line + "\n")
					n += 1
			showinfo("Build Successful", f'{file_name} has been successfully build and stored at location {path + "/dist"}'
			f'\n\nThis Application is built by Rushikesh Powar')

		except CalledProcessError as e:
			showerror("Pyinstaller Error !", f"{e}")


if __name__ == '__main__':
	C = Application()
