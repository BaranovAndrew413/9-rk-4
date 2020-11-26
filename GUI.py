import main as ln
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import pylab
from tkinter import filedialog as fd
# import main as mn


class RungeKuttaGUI:

    def __init__(self, window):
        self.window = window
        self.fig, self.graph_axes = pylab.subplots()
        self.fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)
        self.graph_axes.grid()

    def run(self):
        self.window.title("9-ый номер Баранов")
        self.window.geometry("1000x1000")
        self.mount_components()

    def mount_components(self):
        self.button = ttk.Button(master=self.window, command=self.on_click)
        self.button.configure(text="График")
        self.button.place(x=50, y=0)

        self.button1 = ttk.Button(master=self.window, command=self.table)
        self.button1.configure(text="Таблица")
        self.button1.place(x=150, y=0)

        self.button2 = ttk.Button(master=self.window, command=self.insert_text)
        self.button2.configure(text="Условие задачи 9")
        self.button2.place(x=250, y=0)


        self.r_var = IntVar()
        self.r_var.set(0)
        self.r2 = Radiobutton(tk, text="Func 1", variable=self.r_var, value=1)

        self.error_control = BooleanVar()
        self.error_control.set(0)
        self.error_checkbutton = Checkbutton(
            tk, text="Контроль погрешности", variable=self.error_control, onvalue=1, offvalue=0
        )
        self.error_checkbutton.place(x=50, y=30)

        self.L_label = ttk.Label(self.window)
        self.L_label.configure(text="Условия Задачи Коши")
        self.L_label.place(x=400, y=5)

        self.x0_label = ttk.Label(self.window)
        self.x0_label.configure(text="x0")
        # self.x0_label.pack()
        self.x0_label.place(x=400, y=25)

        self.x0_entry = ttk.Entry(self.window, width=20)
        self.x0_entry.insert(END, 0)
        self.x0_entry.place(x=400, y=50)
        # self.x0_entry.pack()

        self.I0_label = ttk.Label(self.window)
        self.I0_label.configure(text="I0")
        self.I0_label.place(x=400, y=75)

        self.I0_entry = ttk.Entry(self.window, width=20)
        self.I0_entry.insert(END, 0)
        self.I0_entry.place(x=400, y=100)

        self.L_label = ttk.Label(self.window)
        self.L_label.configure(text="Параметры счёта")
        self.L_label.place(x=705, y=5)

        self.h_label = ttk.Label(self.window)
        self.h_label.configure(text="Начальный шаг счета h")
        self.h_label.place(x=705, y=175)

        self.h_entry = ttk.Entry(self.window)
        self.h_entry.insert(END, 0.1)
        self.h_entry.place(x=705, y=200)

        self.x_label = ttk.Label(self.window)
        self.x_label.configure(text="x")
        self.x_label.place(x=705, y=225)

        self.x_entry = ttk.Entry(self.window)
        self.x_entry.insert(END, 1)
        self.x_entry.place(x=705, y=250)

        self.error_label = ttk.Label(self.window)
        self.error_label.configure(text="параметр контроля погрешности")
        self.error_label.place(x=705, y=25)

        self.error_entry = ttk.Entry(self.window)
        self.error_entry.insert(END, 0)
        self.error_entry.place(x=705, y=50)

        self.iter_num_label = ttk.Label(self.window)
        self.iter_num_label.configure(text="максимальное число шагов")
        self.iter_num_label.place(x=705, y=75)

        self.iter_num_entry = ttk.Entry(self.window)
        self.iter_num_entry.insert(END, 0)
        self.iter_num_entry.place(x=705, y=100)

        self.right_limit_label = ttk.Label(self.window)
        self.right_limit_label.configure(text="параметр контроля выхода на правую границу")
        self.right_limit_label.place(x=705, y=125)

        self.right_limit_entry = ttk.Entry(self.window)
        self.right_limit_entry.insert(END, 0)
        self.right_limit_entry.place(x=705, y=150)

        self.L_label = ttk.Label(self.window)
        self.L_label.configure(text="Параметры задачи")
        self.L_label.place(x=550, y=5)

        self.L_label = ttk.Label(self.window)
        self.L_label.configure(text="L")
        self.L_label.place(x=550, y=25)

        self.L_entry = ttk.Entry(self.window, width=20)
        self.L_entry.insert(END, 1)
        self.L_entry.place(x=550, y=50)

        self.R_label = ttk.Label(self.window)
        self.R_label.configure(text="R")
        self.R_label.place(x=550, y=75)

        self.R_entry = ttk.Entry(self.window, width=20)
        self.R_entry.insert(END, 1)
        self.R_entry.place(x=550, y=100)

        self.V_label = ttk.Label(self.window)
        self.V_label.configure(text="V")
        self.V_label.place(x=550, y=125)

        self.V_entry = ttk.Entry(self.window, width=20)
        self.V_entry.insert(END, 1)
        self.V_entry.place(x=550, y=150)


    def on_click(self):
        x0 = int(self.x0_entry.get())
        I0 = int(self.I0_entry.get())
        x = float(self.x_entry.get())
        h = float(self.h_entry.get())
        e = float(self.error_entry.get())
        L = float(self.L_entry.get())
        R = float(self.R_entry.get())
        V = float(self.V_entry.get())
        iter_num = int(self.iter_num_entry.get())
        right_limit = float(self.right_limit_entry.get())


        error_control = self.error_control.get() == 1

        x_values, y_values, _, _, _, _, _, _, _ = ln.func_num_sln(
            x0, I0, x, h, iter_num, e, ln.func_1, error_control, False, L, V, R
        )

        self.draw(x_values, y_values, clear=True)

    def draw(self, x_values, y_values, clear=False):
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

    def insert_text(self):
        self.root = Tk()
        text = open('9.txt', ).readlines()
        text = ''.join(text)
        textline = Text(self.root)
        textline.insert(1.0, text)
        textline.pack()
        self.root.mainloop()

    def output_values(self, max_error, max_h, min_h, n):
        self.root = Tk()
        text = 'Max ЛП = ', max_error, '\n', 'Max h = ', max_h , '\n', 'Min h = ', min_h, 'Количество точек=', n ,\
                '\n' '(x,v)-точка численной траектории, вычисленная методом РК с текущем шагом ',\
                '\n' '(x,v2)-точка численной траектории, вычисленная методом РК с половинным шагом ',\
               '\n'  'ОЛП-оценка локальной погрешности' ,'H-текущий шаг, на котором взяли точку',\
               '\n' 'с1-счетчик деления шага,с2 счетчик удвоений шага'
        # text = ''.join(text)
        textline = Text(self.root)
        textline.insert(1.0, text)
        textline.pack()


    def table(self):
        x0 = int(self.x0_entry.get())
        I0 = int(self.I0_entry.get())
        x = float(self.x_entry.get())
        h = float(self.h_entry.get())
        e = float(self.error_entry.get())
        L = float(self.L_entry.get())
        R = float(self.R_entry.get())
        V = float(self.V_entry.get())
        iter_num = int(self.iter_num_entry.get())
        right_limit = float(self.right_limit_entry.get())

        error_control = self.error_control.get() == 1

        x_values, y1_values, v2, errors, H, c1, c2, _, n = ln.func_num_sln(
            x0, I0, x, h, iter_num, e, ln.func_1, error_control, False, L, V, R
        )
        n=len(x_values)
        data = [i for i in range(0, n)]


        diff = list(map(lambda x: x[0] - x[1], zip(y1_values, v2)))

        values = [
            data,
            x_values,
            y1_values,
            v2,
            errors,
            c1,
            c2,
            H

        ]


        headers = ["№","x", "v", "v2", "ОЛП", "c1", "c2", "H"]

        values_and_headers = [[headers[i]] + data for i, data in enumerate(values)]

        total_rows = len(values_and_headers)
        total_columns = len(values_and_headers[0])

        self.table_root = Tk()
        self.canvas_table = Canvas(self.table_root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas_table, background="#ffffff")
        self.scrollbar = Scrollbar(
            self.table_root, orient="vertical", command=self.canvas_table.yview
        )
        self.canvas_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas_table.pack(side="left", fill="both", expand=True)
        self.canvas_table.create_window((8, 8), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.table = Table(
            self.table_root, self.frame, values_and_headers, total_rows, total_columns
        )

        self.output_values(max(errors), max(H), min(H), n)
    def on_frame_configure(self, event):
        self.canvas_table.configure(scrollregion=self.canvas_table.bbox("all"))

class Table:
    def __init__(self, root, frame, lst, total_rows, total_columns):

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(frame, width=20, fg="black", font=("Arial", 12))

                self.e.grid(row=j, column=i)
                self.e.insert(END, lst[i][j])

if __name__ == "__main__":
    tk = Tk()
    app = RungeKuttaGUI(window=tk)
    app.run()
    tk.mainloop()
