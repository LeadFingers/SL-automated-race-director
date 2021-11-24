import tkinter as tk
import pandas as pd
import openpyxl as pxl

def pilotrankwidget(finallist=[], testdoc = []):
    title = 'Pilot standing widget'
    
    for index in range(0,32):
        finallist.append('pilot' + str(index +1))
        testdoc.append(str(index+1))
    
    
    #Create an instance of Tkinter frame
    win= tk.Tk()

    #Set the geometry of Tkinter frame
    win.geometry("600x950")
    
    #set window color
    #win.configure(bg='light grey')
    
    #set the window title
    win.title(title)

    #import the background image
    background = tk.PhotoImage( file= "images/pilotrank.png")
    
    #create canvas
    width = 600
    height = 950
    mycanvas = tk.Canvas(win, width = width, height = height)
    mycanvas.pack(fill = 'both', expand = True)
    
    #set image in canvas
    mycanvas.create_image(0,0, image = background, anchor = 'nw')
    
    #add a label
    textlines = '-----------------------------------------'
    fillcolor = 'light gray'
    for index in range(0,32):
#         if index > 7:
#             fillcolor = 'light gray'
        mycanvas.create_text(width/16,25*index+130,text=finallist[index],
                             font=("Arial 12 bold"),fill='light gray',anchor = 'nw')
        mycanvas.create_text(width/16,25*index+142,text=textlines,
                             font=("Arial 12"),fill='dark gray',anchor = 'nw')
        mycanvas.create_text(width*8/16,25*index+130,text=testdoc[index],
                             font=("Arial 12 bold"),fill='light gray',anchor = 'nw')

        
#     mycanvas.create_text(width/2, height/8, text = label1, font=("Arial 12 bold"), fill = 'light gray')
#     mycanvas.create_text(width/2, height/4, text = label2, font=("Arial 12 bold"), fill = 'light gray')
#     mycanvas.create_text(width/2, height/5, text = pilotnames, font=("Courier 8"), fill = 'light gray')

    
    win.mainloop()

pilotrankwidget()

def biggobutton(gobuttonstate = True, closeprogramstate = True):
    
    # this class is just for getting info out of the button
    class Buttonoutput(object):
        def __init__(self, gobuttonstate, closeprogramstate):
            self.gobuttonpress = gobuttonstate
            self.closebuttonpress = closeprogramstate
            
        def gobuttoninput(self):
            self.gobuttonpress = not gobuttonstate
        
        def closeprograminput(self):
            self.closebuttonpress = not closeprogramstate
        
    
    #make the button output object
    buttonanswer = Buttonoutput(gobuttonstate, closeprogramstate)    

    #for assigning data to the button output object
    def gobuttonpress():
        buttonanswer.gobuttoninput()
    def closeprogram():
        buttonanswer.closeprograminput()
        
 
    #Create an instance of Tkinter frame
    win= tk.Tk()
    
    #Set the geometry of Tkinter frame
    win.geometry("1280x720")
    
    #set window color
    #win.configure(bg='dark grey')
    
    #set the window title
    title = 'Street League automated race director'
    win.title(title)
    
    #import the background image
    background = tk.PhotoImage( file= "images/background.png")

    #Initialize a Label to display the User Input
    mylabel = tk.Label(win, image = background)
    mylabel.place(x=0, y=0, relwidth = 1, relheight = 1)
    label = 'Press the big button to generate the next round'
    label= tk.Label(win, text=label, font=("Courier 20 bold"), background = '#1d1d1d', fg = 'light gray')
    label.pack()

    #Create a Button to validate Entry Widget
    tk.Button(win, text= "Generate",width= 10, height= 5, font=("Courier 20 bold"), command=
                lambda:[gobuttonpress(), win.destroy()]).pack(padx = 20, pady = 100)
    tk.Button(win, text= "close program",width= 20, height = 2, command=
                lambda:[closeprogram(), win.destroy()]).pack(pady = 100,)


    win.mainloop()
    
    return buttonanswer.gobuttonpress, buttonanswer.closebuttonpress
    
# loopvar = True
# while(loopvar):
#     runprogram = biggobutton()
#     
#     print('go button = ', runprogram[0])
#     print('close button = ', runprogram[1])
#     print('---------------------')
#

def yesornowindow(label1 = '', label2 = '' ,pilotnames = [''],  title = ''):
    
    # this class is just for getting info out of the button
    class Buttonoutput(object):
        def __init__(self,):
            self.yesorno = ''
            
        def buttoninput(self, answer):
            self.yesorno = answer
    
    #make the button output object
    buttonanswer = Buttonoutput()    

    #for assigning data to the button output object
    def clickyes():
        buttonanswer.buttoninput('y')
    def clickno():
        buttonanswer.buttoninput('n')
 
    #Create an instance of Tkinter frame
    win= tk.Tk()

    #Set the geometry of Tkinter frame
    win.geometry("750x250")
    
    #set window color
    #win.configure(bg='light grey')
    
    #set the window title
    win.title(title)

    #import the background image
    background = tk.PhotoImage( file= "images/error.png")
    
    #create canvas
    width = 750
    height = 250
    mycanvas = tk.Canvas(win, width = width, height = height)
    mycanvas.pack(fill = 'both', expand = True)
    
    #set image in canvas
    mycanvas.create_image(0,0, image = background, anchor = 'nw')
    
    #add a label
    mycanvas.create_text(width/2, height/8, text = label1, font=("Arial 12 bold"), fill = 'light gray')
    mycanvas.create_text(width/2, height/4, text = label2, font=("Arial 12 bold"), fill = 'light gray')
    mycanvas.create_text(width/2, height/5, text = pilotnames, font=("Courier 8"), fill = 'light gray')
    
    #add buttons
    button1 = tk.Button(win, text= "Yes",width= 20, command=
              lambda:[clickyes(), win.destroy()])
    button2 = tk.Button(win, text= "No",width= 20, command=
              lambda:[clickno(), win.destroy()])
    
    button1window = mycanvas.create_window(width/5, height*2/3, anchor = 'nw', window = button1)
    button2window = mycanvas.create_window(width*3/5, height*2/3, anchor = 'nw', window = button2)
    
#     #Initialize a Label to display the User Input
#     mylabel = tk.Label(win, image = background)
#     mylabel.place(x=0, y=0, relwidth = 1, relheight = 1)
#     mytext = tk.Label(win, text=label, font=("Courier 10 bold"), background = '#1d1d1d', fg = 'light gray')
#     mytext.pack()
# 
#     #Create a Button to validate Entry Widget
#     tk.Button(win, text= "Yes",width= 20, command=
#               lambda:[clickyes(), win.destroy()]).pack(padx = 100, side = 'left')
#     tk.Button(win, text= "No",width= 20, command=
#               lambda:[clickno(), win.destroy()]).pack(padx = 100, side = 'right')
 
    win.mainloop()
    
    return buttonanswer.yesorno
    
#print(yesornowindow('enter name here'))