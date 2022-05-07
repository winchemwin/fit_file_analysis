from doctest import master
from email.quoprimime import body_length
import tkinter as tk
from tkinter import BOTH, ttk
from tkinter import StringVar, messagebox
from turtle import onclick
from tkinter import filedialog
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from cProfile import label
from lib2to3.pgen2.pgen import DFAState
from msilib.schema import ComboBox
import fitdecode
import seaborn as sns
from tkinter.ttk import Entry


# graph and figure 

def fig_time_dist():
    # fig1=time/distance

    fig = Figure()
    ax = fig.add_subplot(1,1,1)

    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y = dfselec["distance"]
    ax.plot(y)

    ax.set_xlabel('Time/s')
    ax.set_ylabel('Distance/m')
    ax.grid()
    fig.suptitle('Distance/Time')
  
def fig_time_alt():
    # fig2=time/altitude

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y = dfselec["altitude"]
    ax.plot(y)

    ax.set_xlabel('Time/s')
    ax.set_ylabel('Altitude/m')
    ax.grid()
    fig.suptitle('Altitude/Time')

def fig_alt_dist(): 
# fig2-1=distance/altitude

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y = dfselec["altitude"]
    x = dfselec["distance"]

    ax.plot(x, y)

    ax.set_xlabel('Distance/m')
    ax.set_ylabel('Altitude/m')
    ax.grid()
    fig.suptitle('Altitude/Distance')

def fig_time_speed():
    # fig3=time/speed

    fig = Figure()
    ax = fig.add_subplot(1,1,1)

    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y =(3600/1000)*dfselec["speed"]
    ax.plot(y)

    ax.set_xlabel('Time/s')
    ax.set_ylabel('Speed/[km/h]')
    ax.grid()
    fig.suptitle('Speed/Time')
  
def fig_dist_speed():
# fig3-1=distance/speed

    fig = Figure()
    ax = fig.add_subplot(1,1,1)

    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y =(3600/1000)*dfselec["speed"]
    x = dfselec["distance"]
    ax.plot(x, y)

    ax.set_xlabel('Distance/m')
    ax.set_ylabel('Speed/[km/h]')
    ax.grid()
    fig.suptitle('Speed/Distance')

def fig_dist_speed_alt():
    
# fig3-2=distance/speed & altitude
    fig=Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    x = dfselec["distance"]
    y1 =(3600/1000)*dfselec["speed"]
    y2 = dfselec["altitude"]

    ax.plot(x, y1, label='Speed')

    ax2=ax.twinx()
    ax2.plot(x, y2, 'C1', label='Altitude')

    ax.set_xlabel('Distance/m')
    ax.set_ylabel('Speed/[km/h]')
    ax2.set_ylabel('Altitude/m')

    ax.grid()
    fig.suptitle('Speed & Altitude/Distance')

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1+h2, l1+l2)

def fig_time_grade():
    
# fig4=time/grade

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y =dfselec["grade"]
    ax.plot(y)

    ax.set_xlabel('Time/s')
    ax.set_ylabel('grade/%')
    ax.grid()
    fig.suptitle('Grade/Time')

def fig_dist_grade():
    
# fig4-1=distance/grade

    fig = Figure()
    ax = fig.add_subplot(1,1,1)

    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    y =dfselec["grade"]
    x = dfselec["distance"]
    ax.plot(x, y)

    ax.set_xlabel('Distance/s')
    ax.set_ylabel('grade/%')
    ax.grid()
    fig.suptitle('Grade/Distance')

def fig_dist_speed_grade():
# fig4-2=distance/speed & grade
    fig=Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    x = dfselec["distance"]
    y1 =(3600/1000)*dfselec["speed"]
    y2 = dfselec["grade"]

    ax.plot(x, y1, label='Speed')

    ax2=ax.twinx()
    ax2.plot(x, y2,'C1',label='Grade')

    ax.set_xlabel('Distance/m')
    ax.set_ylabel('Speed/[km/h]')
    ax2.set_ylabel('Grade/%')

    ax.grid()
    fig.suptitle('Speed & Grade/Distance')

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()

    ax.legend(h1+h2, l1+l2)

def fig_histgram_time_grade():
    
# fig5=time/grade histgram
    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    x =dfselec["grade"]
    ax.hist(x)

    ax.set_xlabel('grade/%')
    ax.set_ylabel('frequency')

def fig_avespeed_per_grade():
    
    AveSpeeds=[]

    for i in np.linspace(0.5, 18, 36):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        avsp=dfselec[i].mean()
        AveSpeeds.append((3600*avsp/1000))
    
    Avdf=pd.DataFrame(AveSpeeds,index=[np.linspace(0.5, 18, 36)], columns=['Average Speed/km/h'])

    print (Avdf)

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    x=np.linspace(0.5, 18, 36)
    y=AveSpeeds
    ax.bar(x, y)

    ax.set_xlabel('grade/%')
    ax.set_ylabel('Average Speed/km/h')

def fig_sumdist_per_grade():
    Sumdist=[]
    ForStd=[]

    for i in np.linspace(3.0, 18, 31):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist=dfselec[i].sum()
        Sumdist.append(sumdist)
    
        for n in range(int(sumdist)):
            ForStd.append(i)
    
    print ('Average grade=','{:.2f}'.format(np.average(ForStd)),'%')
    print ('Standard deviation=', '{:.2f}'.format(np.std(ForStd)),'%')

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    x=np.linspace(3.0, 18, 31)
    y=Sumdist
    ax.bar(x, y)

    ax.set_xlabel('grade/%')
    ax.set_ylabel('Distance/m')

def fig_boxplot():
    Sumdist=[]
    ForStd=[]

    for i in np.linspace(3.0, 18, 31):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist=dfselec[i].sum()
        Sumdist.append(sumdist)
    
        for n in range(int(sumdist)):
            ForStd.append(i)
    
    # Fig 8 Box plot

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    ax.boxplot(ForStd)

    ax.set_xlabel('Saka1')
    ax.set_ylabel('grade/%')

def fig_violineplot():
    Sumdist=[]
    ForStd=[]

    for i in np.linspace(3.0, 18, 31):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist=dfselec[i].sum()
        Sumdist.append(sumdist)
    
        for n in range(int(sumdist)):
            ForStd.append(i)
    
    # Fig 9 violineplot

    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    
    fig_canvas = FigureCanvasTkAgg (fig, master=sub_window1)
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(fig_canvas, sub_window1)
    toolbar.update()
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    ax.violinplot(ForStd)

    ax.set_xlabel('Saka1')
    ax.set_ylabel('grade/%')

def Gekizaka_factor():
    #Gekizaka(grade) factor

    Sumdist36=[]
    for i in np.linspace(3.0, 6.0, 7):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist36=dfselec[i].sum()
        Sumdist36.append(sumdist36)
    
    Sumdist69=[]
    for i in np.linspace(6.5, 9.0, 6):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist69=dfselec[i].sum()
        Sumdist69.append(sumdist69)
    
    Sumdist912=[]
    for i in np.linspace(9.5, 12, 6):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist912=dfselec[i].sum()
        Sumdist912.append(sumdist912)

    Sumdist1215=[]
    for i in np.linspace(12.5, 15, 6):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist1215=dfselec[i].sum()
        Sumdist1215.append(sumdist1215)   

    Sumdist1518=[]
    for i in np.linspace(15.5, 18, 6):
        dfselec[i]=dfselec.loc[dfselec["grade"]==i, 'speed']
        sumdist1518=dfselec[i].sum()
        Sumdist1518.append(sumdist1518)       

    Gekizaka_Factor1=sum(Sumdist1518)/(sum(Sumdist36)+sum(Sumdist69)+sum(Sumdist912)+sum(Sumdist1215)+sum(Sumdist1518))
    Gekizaka_Factor2=sum(Sumdist1215)/(sum(Sumdist36)+sum(Sumdist69)+sum(Sumdist912)+sum(Sumdist1215)+sum(Sumdist1518))
    Gekizaka_Factor3=sum(Sumdist912)/(sum(Sumdist36)+sum(Sumdist69)+sum(Sumdist912)+sum(Sumdist1215)+sum(Sumdist1518))
    Gekizaka_Factor4=(sum(Sumdist912)+2*sum(Sumdist1215)+3*sum(Sumdist1518))/(sum(Sumdist36)+sum(Sumdist69)+sum(Sumdist912)+sum(Sumdist1215)+sum(Sumdist1518))
    Gekizaka_Factor5=((0.5*sum(Sumdist36)+sum(Sumdist69)+1.5*sum(Sumdist912)+3*sum(Sumdist1215)+5*sum(Sumdist1518))/(sum(Sumdist36)+sum(Sumdist69)+sum(Sumdist912)+sum(Sumdist1215)+sum(Sumdist1518)))

    Message1=tk.Message(sub_window1,text=f'Gekizaka Factor1:{Gekizaka_Factor1:.2f}',width=300,font=("メイリオ","12","bold"))
    Message1.place(x=20, y=20)
    Message2=tk.Message(sub_window1,text=f'Gekizaka Factor2:{Gekizaka_Factor2:.2f}',width=300,font=("メイリオ","12","bold"))
    Message2.place(x=20, y=50)
    Message3=tk.Message(sub_window1,text=f'Gekizaka Factor3:{Gekizaka_Factor3:.2f}',width=300, font=("メイリオ","12","bold"))
    Message3.place(x=20, y=80)
    Message4=tk.Message(sub_window1,text=f'Gekizaka Factor4:{Gekizaka_Factor4:.2f}',width=300,font=("メイリオ","12","bold"))
    Message4.place(x=20, y=110)
    Message5=tk.Message(sub_window1,text=f'Gekizaka Factor5:{Gekizaka_Factor5:.2f}',width=300, font=("メイリオ","12","bold"))
    Message5.place(x=20, y=140)

def disp_selsctarea():
    
    startdist=startdist_iv.get()
    enddist=enddist_iv.get()
    
    global dfselec
    dfselec=df[(startdist<df["distance"]) & (df["distance"]<enddist)]
      
    fig2 = plt.figure(figsize=(4,2), dpi=50)
    ax = fig2.add_subplot(1,1,1)

    y = dfselec["altitude"]
    x = dfselec["distance"]
    
    ax.plot(x, y)
    ax.set_xlabel('Distance/m')
    ax.set_ylabel('Altitude/m')
    ax.grid()
    fig2.suptitle('Altitude/Distance') 
    
    fig_canvas2 = FigureCanvasTkAgg (fig2, master=root)
    fig_canvas2.get_tk_widget().place(x=350,y=150, width=430, height=210)
    
    Label20=ttk.Label(root, text=u'Analysis area',font=("Arial","10","bold"))
    Label20.place(x=500, y=120)
    
    sub_window1.destroy()

def data_select():
 
    filename=filename_sv.get()
   
    datas = []
    with fitdecode.FitReader(filename) as fit:
        for frame in fit:

            if isinstance(frame, fitdecode.FitDataMessage):
                if frame.name == 'record':
                    data = {}
                    for field in frame.fields:
                        data[field.name] = field.value
                        data[field.name + '_units'] = field.units
                    datas.append(data)
    global df
    df=pd.DataFrame(datas) 
    
    # Sub window
    global sub_window1
    sub_window1=tk.Toplevel()
    sub_window1.title('Graph, Analyzed results')
    sub_window1.geometry('720x540')
    
    fig1 = Figure()
    ax = fig1.add_subplot(1,1,1)
    
    fig_canvas1 = FigureCanvasTkAgg (fig1, master=sub_window1)
    fig_canvas1.get_tk_widget().place(x=30,y=50, width=600, height=400)

    y = df["altitude"]
    x = df["distance"]

    ax.plot(x, y)

    ax.set_xlabel('Distance/m')
    ax.set_ylabel('Altitude/m')
    ax.grid()
    fig1.suptitle('Altitude/Distance')
    
    LabelS_1=ttk.Label(sub_window1, text=u'Setting of analysis area', font=("Arial","12","bold"))
    LabelS_1.place(x=10, y=5, width=200, height=40)
    
    LabelS_2=ttk.Label(sub_window1, text=u'Start point (m)', font=("Times","10","bold"))
    LabelS_2.place(x=30, y=460, width=200)
    global startdist_iv
    startdist_iv=tk.IntVar()
    textBoxS_1=ttk.Entry(sub_window1, width=30, textvariable=startdist_iv)
    textBoxS_1.place(x=30, y=490)
    
    LabelS_3=ttk.Label(sub_window1, text=u'End point (m)', font=("Times","10","bold"))
    LabelS_3.place(x=230, y=460, width=200)
    global enddist_iv
    enddist_iv=tk.IntVar()
    textBoxS_2=ttk.Entry(sub_window1, width=30, textvariable=enddist_iv)
    textBoxS_2.place(x=230, y=490)
    LabelS_4=ttk.Label(sub_window1, text=u'Selected area Ok ? ')
    LabelS_4.place(x=500, y=460, width=150)
           
    ButtonS_1=ttk.Button(sub_window1, text=u'Ok, Execute',width=20, command=disp_selsctarea)
    ButtonS_1.place(x=550, y=490)

    
# Data analysis
def data_analysis ():

    treatment=treatment_sv.get()
    
    #  Sub window
    global sub_window1
    sub_window1=tk.Toplevel()
    sub_window1.title('Graph, Analyzed results')
    sub_window1.geometry('720x540')
    

    #  Selection of works
    
    if treatment=='distande/time':
        fig_time_dist()
        
    elif treatment=='altitude/time':
        fig_time_alt()
        
    elif treatment=='altitude/distance':
        fig_alt_dist()

    elif treatment=='time/speed':
        fig_time_speed()

    elif treatment=='distance/speed':
        fig_dist_speed()

    elif treatment=='distance/speed&altitude':
       fig_dist_speed_alt()

    elif treatment=='time/grade':
        fig_time_grade()

    elif treatment=='distance/grade':
        fig_dist_grade()

    elif treatment=='distance/speed&grade':
       fig_dist_speed_grade()
    
    elif treatment=='histogram_time/grade':
       fig_histgram_time_grade()   
    
    elif treatment=='ave_speed/grade':
        fig_avespeed_per_grade()
    
    elif treatment=='Sum of distance/grade':
        fig_sumdist_per_grade()   
        
    elif treatment=='Box plot':
        fig_boxplot()
        
    elif treatment=='Violine plot':
        fig_violineplot()
    
    elif treatment=='Saka(slope) factor':
        Gekizaka_factor()
    
#　Tkinter main 

root = tk.Tk()
root.title("Fit Data Analysis")
root.geometry('800x600')

# Selection of a file
def data_import(file):
    
    type = [('fit file', '*.fit')] 
    file = filedialog.askopenfilename(filetypes = type)
    filename_sv.set(file)
    filename=filename_sv.get()

    
# finish program
def scry_finish():
    exit()
    
# Save data
def data_save():
    type = [('csv file','*.csv')]
    file =filedialog.asksaveasfilename(filetypes=type)
    filename_sv.set(file)
    filename=filename_sv.get()
    df.to_csv(filename +'.csv')

Label0=ttk.Label(root, text=u'Analysis of a fit file', font=("Arial","12","bold"))
Label0.place(x=10, y=5, width=300, height=40)
Label1=ttk.Label(root, text=u'Select a file',font=("Times","11","bold"))
Label1.place(x=20, y=40)
filename_sv = tk.StringVar()
filenameEntry = ttk.Entry(width=120, text="", textvariable=filename_sv)
filenameEntry.place(x=20, y= 60)
    
Button1 = ttk.Button(text=u'Select',width=20)
Button1.bind("<Button-1>", data_import) 
Button1.place(x=20, y=90)

Label1_1=ttk.Label(root, text=u'Set of analysis area',font=("Times","11","bold"))
Label1_1.place(x=20, y=130)
Label1_2=ttk.Label(root, text=u'Drawing of graph(Altitude/Distance) and select analysis area)', font=("Times","8"))
Label1_2.place(x=20, y=150)

Button1_1=ttk.Button(text=u'Execute of selection',width=20, command=data_select)
Button1_1.place(x=20, y=170)

# プルダウンメニューの作成
graphs=('distande/time', 'altitude/time', 'altitude/distance','time/speed',
        'distance/speed','distance/speed&altitude','time/grade','distance/grade',
        'distance/speed&grade','histogram_time/grade','ave_speed/grade',
        'Sum of distance/grade','Box plot','Violine plot','Saka(slope) factor')
treatment_sv = tk.StringVar()
Label3=ttk.Label(text=u'Select a executig work', font=("Times","11","bold"))
Label3.place(x=20, y=380)

ComboBox1=ttk.Combobox(root, height=5, width=20, state='readonly', values=graphs, textvariable=treatment_sv)
ComboBox1.place(x=20, y=410)


Label5=ttk.Label(text=u'Selected work is Ok ?', font=("Times","11","bold"))
Label5.place(x=20, y=440)
Button2 = ttk.Button(text=u'Execute',width=20, command=data_analysis)
Button2.place(x=20, y=470)

Label7=ttk.Label(text=u'Finish the program')
Label7.place(x=650, y=550)
Button3 = ttk.Button(text=u'Finish',width=20, command=scry_finish)
Button3.place(x=650, y=570)

Label8=ttk.Label(text=u'Save analyzed data（csv)')
Label8.place(x=20, y=550)
Button4 = ttk.Button(text=u'Execute',width=20, command=data_save)
Button4.place(x=20, y=570)

root.mainloop()

