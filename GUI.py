import main as ln
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

from tkinter import ttk
import pylab
# import main as mn


class RungeKuttaGUI:
	def __init__(self, window):
		self.window = window
		self.fig, self.graph_axes = pylab.subplots()
		self.fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)
		self.graph_axes.grid()

	def run(self):
		self.window.title('Runge Kutta')
		self.window.geometry("700x700")
		self.mount_components()

	def mount_components(self):
		self.button = ttk.Button(master=self.window, command=self.on_click)
		self.button.configure(text='Graph')
		self.button.place(x=50, y=0)

		self.button1 = ttk.Button(master=self.window, command=self.table)
		self.button1.configure(text='Table')
		self.button1.place(x=150, y=0)

		self.r_var = IntVar()
		self.r_var.set(0)
		self.r1 = Radiobutton(tk, text='Test Func', variable=self.r_var, value=0)
		self.r2 = Radiobutton(tk, text='Func 1', variable=self.r_var, value=1)
		self.r3 = Radiobutton(tk, text='Func 2', variable=self.r_var, value=2)
		self.r1.place(x=250, y=0)
		self.r2.place(x=250, y=25)
		self.r3.place(x=250, y=50)

		self.error_control = BooleanVar()
		self.error_control.set(0)
		self.error_checkbutton = Checkbutton(tk, text="Error control", variable=self.error_control, onvalue=1,
											 offvalue=0)
		self.error_checkbutton.place(x=50, y=30)

		self.x0_label = ttk.Label(self.window)
		self.x0_label.configure(text='x0')
		# self.x0_label.pack()
		self.x0_label.place(x=400, y=25)

		self.x0_entry = ttk.Entry(self.window, width=20)
		self.x0_entry.insert(END, 0)
		self.x0_entry.place(x=400, y=50)
		# self.x0_entry.pack()

		self.y0_label = ttk.Label(self.window)
		self.y0_label.configure(text='y0')
		self.y0_label.place(x=400, y=75)

		self.y0_entry = ttk.Entry(self.window, width=20)
		self.y0_entry.insert(END, 1)
		self.y0_entry.place(x=400, y=100)

		self.h_label = ttk.Label(self.window)
		self.h_label.configure(text='h')
		self.h_label.place(x=400, y=125)

		self.h_entry = ttk.Entry(self.window)
		self.h_entry.insert(END, 0.1)
		self.h_entry.place(x=400, y=150)

		self.x_label = ttk.Label(self.window)
		self.x_label.configure(text='x')
		self.x_label.place(x=400, y=175)

		self.x_entry = ttk.Entry(self.window)
		self.x_entry.insert(END, 1)
		self.x_entry.place(x=400, y=200)

		self.error_label = ttk.Label(self.window)
		self.error_label.configure(text='error')
		self.error_label.place(x=50, y=55)

		self.error_entry = ttk.Entry(self.window)
		self.error_entry.insert(END, 0)
		self.error_entry.place(x=50, y=80)

		self.iter_num_label = ttk.Label(self.window)
		self.iter_num_label.configure(text='Iteration number')
		self.iter_num_label.place(x=50, y=115)

		self.iter_num_entry = ttk.Entry(self.window)
		self.iter_num_entry.insert(END, 0)
		self.iter_num_entry.place(x=50, y=140)

		self.right_limit_label = ttk.Label(self.window)
		self.right_limit_label.configure(text='Right limit')
		self.right_limit_label.place(x=50, y=175)

		self.right_limit_entry = ttk.Entry(self.window)
		self.right_limit_entry.insert(END, 0)
		self.right_limit_entry.place(x=50, y=200)

		self.a_label = ttk.Label(self.window)
		self.a_label.configure(text='a')
		self.a_label.place(x=550, y=25)

		self.a_entry = ttk.Entry(self.window, width=20)
		self.a_entry.insert(END, 1)
		self.a_entry.place(x=550, y=50)

		self.b_label = ttk.Label(self.window)
		self.b_label.configure(text='b')
		self.b_label.place(x=550, y=75)

		self.b_entry = ttk.Entry(self.window, width=20)
		self.b_entry.insert(END, 1)
		self.b_entry.place(x=550, y=100)

	def on_click(self):
		x0 = int(self.x0_entry.get())
		y0 = int(self.y0_entry.get())
		x = float(self.x_entry.get())
		h = float(self.h_entry.get())
		e = float(self.error_entry.get())
		a = float(self.a_entry.get())
		b = float(self.b_entry.get())
		iter_num = int(self.iter_num_entry.get())
		right_limit = float(self.right_limit_entry.get())
		if self.r_var.get() == 0:
			self.graph_axes.clear()
			clear = False
			data = ln.test_precise_sln(x0, y0, h, x)
			x_values = data[0].copy()
			y_values = data[1].copy()
			self.draw(x_values, y_values, clear)
			if self.error_control.get() == 1:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_test, True, True)
				x_values = data[0].copy()
				y_values = data[1].copy()
			else:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_test, False, True)
				x_values = data[0].copy()
				y_values = data[1].copy()
			self.draw(x_values, y_values, clear)
		elif self.r_var.get() == 1:
			clear = True
			if self.error_control.get() == 1:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_1, True, True)
				x_values = data[0].copy()
				y_values = data[1].copy()
			else:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_1, False, True)
				x_values = data[0].copy()
				y_values = data[1].copy()
			self.draw(x_values, y_values, clear)
		elif self.r_var.get() == 2:
			self.graph_axes.clear()
			clear = False
			if self.error_control.get() == 1:
				data = ln.num_sol_3_task(a, b, iter_num, ln.f_1, ln.f_2, x0, y0, y0, x, h, e, True)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				y2_values = data[7].copy()
				self.draw(x_values, y1_values, clear)
				self.draw(x_values, y2_values, clear)
			else:
				data = ln.num_sol_3_task(a, b, iter_num, ln.f_1, ln.f_2, x0, y0, y0, x, h, e, False)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				y2_values = data[7].copy()
				self.draw(x_values, y1_values, clear)
				self.draw(x_values, y2_values, clear)

	# self.draw(x_values, y_values, clear)

	def draw(self, x_values, y_values, clear):
		if clear:
			self.graph_axes.clear()
		self.graph_axes.plot(x_values, y_values)
		try:
			self.canvas.get_tk_widget().pack_forget()
		except AttributeError:
			pass
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
		self.canvas.draw()
		self.canvas.get_tk_widget().place(x=0, y=250)

	def table(self):
		x0 = int(self.x0_entry.get())
		y0 = int(self.y0_entry.get())
		x = float(self.x_entry.get())
		h = float(self.h_entry.get())
		e = float(self.error_entry.get())
		a = float(self.a_entry.get())
		b = float(self.b_entry.get())
		iter_num = int(self.iter_num_entry.get())
		right_limit = float(self.right_limit_entry.get())
		count = []
		if self.r_var.get() == 0:
			if self.error_control.get() == 1:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_test, True, True)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				v2 = data[2].copy()
				errors = data[3].copy()
				h = data[4].copy()
				c1 = data[5].copy()
				c2 = data[6].copy()

			else:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_test, False, True)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				v2 = data[2].copy()
				errors = data[3].copy()
				h = data[4].copy()
				c1 = data[5].copy()
				c2 = data[6].copy()
		elif self.r_var.get() == 1:
			if self.error_control.get() == 1:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_1, True, True)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				v2 = data[2].copy()
				errors = data[3].copy()
				h = data[4].copy()
				c1 = data[5].copy()
				c2 = data[6].copy()
			else:
				data = ln.func_num_sln(x0, y0, x, h, iter_num, e, ln.func_1, False, True)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				v2 = data[2].copy()
				errors = data[3].copy()
				h = data[4].copy()
				c1 = data[5].copy()
				c2 = data[6].copy()
		elif self.r_var.get() == 2:
			if self.error_control.get() == 1:
				data = ln.num_sol_3_task(a, b, iter_num, ln.f_1, ln.f_2, x0, y0, y0, x, h, e, True)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				y2_values = data[7].copy()
			else:
				data = ln.num_sol_3_task(a, b, iter_num, ln.f_1, ln.f_2, x0, y0, y0, x, h, e, False)
				x_values = data[0].copy()
				y1_values = data[1].copy()
				y2_values = data[7].copy()

		diff = list(map(lambda x: x[0] - x[1], zip(y1_values, v2)))
		if not count:
			count = [''] * len(errors)
		values = [x_values, y1_values, v2, diff, errors, [max(errors)] * len(errors), c1, c2, [h] * len(errors), count]
		print(count)
		total_rows = len(values)
		total_columns = len(values[0])

		self.table_root = Tk()
		self.canvas_table = Canvas(self.table_root, borderwidth=0, background="#ffffff")
		self.frame = Frame(self.canvas_table, background="#ffffff")
		self.scrollbar = Scrollbar(self.table_root, orient="vertical", command=self.canvas_table.yview)
		self.canvas_table.configure(yscrollcommand=self.scrollbar.set)
		self.scrollbar.pack(side="right", fill="y")
		self.canvas_table.pack(side="left", fill="both", expand=True)
		self.canvas_table.create_window((8, 8), window=self.frame, anchor="nw")
		self.frame.bind("<Configure>", self.on_frame_configure)

		self.table = Table(self.table_root, self.frame, values, total_rows, total_columns)

	def on_frame_configure(self, event):
		self.canvas_table.configure(scrollregion=self.canvas_table.bbox("all"))


class Table:

	def __init__(self, root, frame, lst, total_rows, total_columns):

		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				self.e = Entry(frame, width=30, fg='black',
							   font=('Arial', 12))

				self.e.grid(row=j, column=i)
				self.e.insert(END, lst[i][j])


if __name__ == "__main__":
	tk = Tk()
	app = RungeKuttaGUI(window=tk)
	app.run()
	tk.mainloop()