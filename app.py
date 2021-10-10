from tkinter import *
from tkinter import filedialog
from fpdf import FPDF


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf,'r',encoding="utf8")  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

ws = Tk()
ws.title("Txt viewer and converter")
ws.geometry("800x850")
ws['bg']='#3EB489'

txtarea = Text(ws, width=120, height=40)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=50)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

def conv(file_name):

    pdf = FPDF()   
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    fg=str(file_name)+'.txt'
    # open the text file in read mode
    f = open(fg, "r",encoding='utf-8')
    
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
    
    # save the pdf with name .pdf
    pdf.output("my.pdf") 



def convert_text():
    global e
    string = e.get() 
    if bool(string):
        conv(string)


ws.title('Name')

e = Entry(ws)
e.pack()
e.focus_set()

b = Button(ws,text='turn to pdf',command=convert_text)
b.pack(side='top')


# def conv(file_name):

#     pdf = FPDF()   
    
#     # Add a page
#     pdf.add_page()
    
#     # set style and size of font 
#     # that you want in the pdf
#     pdf.set_font("Arial", size = 15)
#     fg=str(file_name)+'.txt'
#     # open the text file in read mode
#     f = open(fg, "r",encoding='utf-8')
    
#     for x in f: 
#         pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
    
#     # save the pdf with name .pdf
#     pdf.output("my.pdf") 






ws.mainloop()

