import cv2
from tkinter import *
import numpy as np
from tkinter import messagebox
from tkinter.filedialog import askopenfile


class Application(Frame):
    def __init__(self, root):
        super(Application, self).__init__(root)
        self.root = root
        self.config()
        self.create_widgets()
    def create_widgets(self):
        #Кнопка запуска вебкамеры
        self.but_Webcam = Button(self, text="Запуск вебкамеры", command=self.Start_Webcam, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_Webcam.place(x = 50 , y = 50)

        #Кнопка запуска видео с файла
        self.but_Video = Button(self, text="Запуск видео с файла", command=self.Start_Video, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_Video.place(x = 550 ,y = 50)

        #Кнопка запуска вебкамеры с геометрическим преобразованием(Зеркальное отображение)
        self.but_Mirror_Webcam = Button(self, text="Зеркальное отобр.(Web)", command=self.Mirror_Webcam, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_Mirror_Webcam.place(x = 50 ,y = 150)

        #Кнопка запуска видео с файла с геометрическим преобразова-нием(Зеркальное отображение)
        self.but_Mirror_Video = Button(self, text="Зеркальное отобр.(Vid)", command=self.Mirror_Video, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_Mirror_Video.place(x = 550 ,y = 150)

        #Кнопка запуска вебкамеры с цветовым преобразованием(LAB)
        self.but_LAB_Webcam = Button(self, text="Вебкамера(LAB)", command=self.LAB_Webcam, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_LAB_Webcam.place(x = 50 ,y = 450)

        #Кнопка запуска видео с файла с цветовым преобразованием(LAB)
        self.but_LAB_Video = Button(self, text="Видео с файла(LAB)", command=self.LAB_Video, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_LAB_Video.place(x = 550 ,y = 450)

        #Поле "Вебкамера с ВЧ"
        self.label_VCH_Webcam = Label(self, text="Вебкамера с ВЧ", width = 20, height = 2, bg = "steelblue", relief = GROOVE)
        self.label_VCH_Webcam.place(x = 50 ,y = 250)

        #Поле "Видео с ВЧ"
        self.label_VCH_Video = Label(self, text="Видео с ВЧ", width = 20, height = 2, bg = "steelblue", relief = GROOVE)
        self.label_VCH_Video.place(x = 550 ,y = 250)

        #Кнопка для выбора видео с файла
        self.but_Open_File = Button(self, text="Открыть файл", command=self.openfile, width = 20, height = 2, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but_Open_File.place(x = 300 ,y = 50)

        #Поле "Растягивание(Вебка)"
        self.label_Stretching_Webcam = Label(self, text="Растягивание(Вебка)", width = 20, height = 2, bg = "steelblue", relief = GROOVE)
        self.label_Stretching_Webcam.place(x = 50 ,y = 350)

        #Поле "Растягивание(Видео)"
        self.label_Stretching_Video = Label(self, text="Растягивание(Видео)", width = 20, height = 2, bg = "steelblue", relief = GROOVE)
        self.label_Stretching_Video.place(x = 550 ,y = 350)

        #Маркер для вызова настройки доп. параметров ВЧ(Вебкамера)
        self.cb_VCH_Webcam = Checkbutton(self, variable=self.var, command=self.onClick,  height=1,bg = "steelblue" , relief = GROOVE)
        self.cb_VCH_Webcam.place(x=200, y=250)

        #Маркер для вызова настройки доп. параметров Растягивание(Вебкамера)
        self.cb_Stretching_Webcam = Checkbutton(self, variable=self.var1, command=self.onClick1, height=1, bg="steelblue", relief = GROOVE)
        self.cb_Stretching_Webcam.place(x=200, y=350)

        #Маркер для вызова настройки доп. параметров ВЧ(Видео)
        self.cb_VCH_Video = Checkbutton(self, variable=self.var2, command=self.onClick2, height=1, bg="steelblue", relief = GROOVE)
        self.cb_VCH_Video.place(x=700, y=250)

        #Маркер для вызова настройки доп. параметров Растягивание(Видео)
        self.cb_Stretching_Video = Checkbutton(self, variable=self.var3, command=self.onClick3, height=1, bg="steelblue", relief = GROOVE)
        self.cb_Stretching_Video.place(x=700, y=350)

    def config(self):
        self.pack(fill=BOTH, expand=1)
        self.var = BooleanVar()
        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()


    def onClick(self):
        if self.var.get() == True:
            self.VCH_Webcam_DLC()
        else:
            self.K1_entr.destroy()
            self.but5.destroy()

    def onClick1(self):
        if self.var1.get() == True:
            self.Stretching_Webcam_DLC()
        else:
            self.K2_entr.destroy()
            self.but6.destroy()

    def onClick2(self):
        if self.var2.get() == True:
            self.VCH_Video_DLC()
        else:
            self.K3_entr.destroy()
            self.but7.destroy()

    def onClick3(self):
        if self.var3.get() == True:
            self.Stretching_Video_DLC()
        else:
            self.K4_entr.destroy()
            self.but8.destroy()

    def Start_Webcam(self):
        cv2.namedWindow("WEBCAM")
        vc = cv2.VideoCapture(0)
        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            cv2.imshow("WEBCAM", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        cv2.destroyWindow("WEBCAM")
        vc.release()

    def Start_Video(self):
        try:
            cap = self.videofile
        except:
            messagebox.showerror("Ошибка", "Для начала нужно выбрать файл!")
        else:
            while True:
                if cap.grab():
                    flag, frame = cap.retrieve()
                    if not flag:
                        continue
                    else:
                        cv2.imshow('VIDEO', frame)
                if cv2.waitKey(10) == 27:
                    break

    def Mirror_Webcam(self):
        cv2.namedWindow("Mirror_Webcam")
        vc = cv2.VideoCapture(0)
        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False
        while rval:

            rows, cols = frame.shape[:2]

            src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
            dst_points = np.float32([[cols - 1, 0], [0, 0], [cols - 1, rows - 1]])

            affine_matrix = cv2.getAffineTransform(src_points, dst_points)
            img_output = cv2.warpAffine(frame, affine_matrix, (cols, rows))

            cv2.imshow("Mirror_Webcam", img_output)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        cv2.destroyWindow("Mirror_Webcam")
        vc.release()

    def Mirror_Video(self):
        try:
            cap = self.videofile
        except:
            messagebox.showerror("Ошибка", "Для начала нужно выбрать файл!")
        else:
            while True:
                if cap.grab():
                    flag, frame = cap.retrieve()
                    rows, cols = frame.shape[:2]

                    src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
                    dst_points = np.float32([[cols - 1, 0], [0, 0], [cols - 1, rows - 1]])

                    affine_matrix = cv2.getAffineTransform(src_points, dst_points)

                    if not flag:
                        continue
                    else:
                        img_output = cv2.warpAffine(frame, affine_matrix, (cols, rows))
                        cv2.imshow('Mirror_Video', img_output)
                if cv2.waitKey(10) == 27:
                    break

    def LAB_Webcam(self):
        cv2.namedWindow("LAB_Webcam")
        vc = cv2.VideoCapture(0)
        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            LAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            cv2.imshow("LAB_Webcam", LAB)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        cv2.destroyWindow("LAB_Webcam")
        vc.release()

    def LAB_Video(self):
        try:
            cap = self.videofile
        except:
            messagebox.showerror("Ошибка", "Для начала нужно выбрать файл!")
        else:
            while True:
                if cap.grab():
                    flag, frame = cap.retrieve()
                    if not flag:
                        continue
                    else:
                        LAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
                        cv2.imshow('LAB_Video', LAB)
                if cv2.waitKey(10) == 27:
                    break

    def VCH_Webcam_DLC(self):
        self.K1_entr = Entry(self)
        self.K1_entr.place(x = 50 ,y = 300)
        self.but5 = Button(self, text="Start", command=self.VCH_Webcam, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but5.place(x = 180 ,y = 300)

    def VCH_Video_DLC(self):
        self.K3_entr = Entry(self)
        self.K3_entr.place(x = 550 ,y = 300)
        self.but7 = Button(self, text="Start", command=self.VCH_Video, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but7.place(x = 680 ,y = 300)

    def VCH_Webcam(self):
        try:
            K = float(self.K1_entr.get())
        except:
            messagebox.showerror("Ошибка", "Значение фильтра должно быть чис-лом!")
        else:
            if K >= 1 and K <= 15:
                cv2.namedWindow("VCH Webcam")
                vc = cv2.VideoCapture(0)

                if vc.isOpened():  # try to get the first frame
                    rval, frame = vc.read()
                else:
                    rval = False
                while rval:
                    kernel_indentity = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, 1]])* K
                    output = cv2.filter2D(frame, -1, kernel_indentity)
                    cv2.imshow("VCH Webcam", output)
                    rval, frame = vc.read()
                    key = cv2.waitKey(20)
                    if key == 27:  # exit on ESC
                        break
                cv2.destroyWindow("VCH Webcam")
                vc.release()
            else:
                messagebox.showerror("Ошибка", "Значение фильтра должно быть в диапазоне (1-15)!")

    def VCH_Video(self):
        try:
            K = float(self.K3_entr.get())
        except:
            messagebox.showerror("Ошибка", "Значение фильтра должно быть чис-лом!")
        else:
            if K >= 1 and K <= 15:
                try:
                    cap = self.videofile
                except:
                    messagebox.showerror("Ошибка", "Для начала нужно выбрать файл!")
                else:
                    while True:
                        if cap.grab():
                            flag, frame = cap.retrieve()
                            kernel_indentity = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, 1]]) * K
                            if not flag:
                                continue
                            else:
                                output = cv2.filter2D(frame, -1, kernel_indentity)
                                cv2.imshow('VCH Video', output)
                        if cv2.waitKey(10) == 27:
                            break
            else:
                messagebox.showerror("Ошибка", "Значение фильтра должно быть в диапазоне (1-15)!")


    def Stretching_Webcam_DLC(self):
        self.K2_entr = Entry(self)
        self.K2_entr.place(x = 50, y = 400)
        self.but6 = Button(self, text="Start", command=self.Stretching_Webcam, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but6.place(x = 180, y = 400)

    def Stretching_Video_DLC(self):
        self.K4_entr = Entry(self)
        self.K4_entr.place(x = 550, y = 400)
        self.but8 = Button(self, text="Start", command=self.Stretching_Video, bg = "steelblue", activebackground = "deepskyblue", activeforeground = "blue", relief = GROOVE)
        self.but8.place(x = 680, y = 400)

    def Stretching_Webcam(self):
        try:
            K = int(self.K2_entr.get())
        except:
            messagebox.showerror("Ошибка", "Значение фильтра должно быть целым числом!")
        else:
            if K >= 0 and K <= 30:
                cv2.namedWindow("Stretching_Webcam")
                vc = cv2.VideoCapture(0)
                if vc.isOpened():  # try to get the first frame
                    rval, frame = vc.read()
                else:
                    rval = False
                while rval:
                    kernel = np.ones((5, 5), np.uint8)
                    img_dilation = cv2.dilate(frame, kernel, iterations= K)
                    cv2.imshow("Stretching_Webcam", img_dilation)
                    rval, frame = vc.read()
                    key = cv2.waitKey(20)
                    if key == 27:  # exit on ESC
                        break
                cv2.destroyWindow("Stretching_Webcam")
                vc.release()
            else:
                messagebox.showerror("Ошибка", "Значение фильтра должно быть в диапазоне (0-30)!")

    def Stretching_Video(self):
        try:
            K = int(self.K4_entr.get())
        except:
            messagebox.showerror("Ошибка", "Значение фильтра должно быть целым числом!")
        else:
            if K >= 0 and K <= 30:
                try:
                    cap = self.videofile
                except:
                    messagebox.showerror("Ошибка", "Для начала нужно выбрать файл!")
                else:
                    while True:
                        if cap.grab():
                            flag, frame = cap.retrieve()
                            kernel = np.ones((5, 5), np.uint8)
                            if not flag:
                                continue
                            else:
                                img_dilation = cv2.dilate(frame, kernel, iterations=K)
                                cv2.imshow('Stretching_Video', img_dilation)
                        if cv2.waitKey(10) == 27:
                            break
            else:
                messagebox.showerror("Ошибка", "Значение фильтра должно быть в диапазоне (0-30)!")

    def openfile(self):
        fopen = askopenfile(mode='rb', defaultextension=".mp4", filetypes=(("Video files", "*.mp4"), ("All files", "*.*")))
        if fopen == None: return
        self.videofile = cv2.VideoCapture(fopen.name)

root = Tk()
root.geometry("750x550")
root.title("Exam")
app = Application(root)
app.configure(background = 'pink')
root.mainloop()
