import tkinter as tk
import pandas as pd
import openpyxl as pxl
import mainscript as main

def pilotrankwidget(gobuttonstate = True, closeprogramstate = True, finallist = ['']):
# def pilotrankwidget():
    
    # this class is just for getting info out of the button
    class Buttonoutput(object):
        def __init__(self, gobuttonstate, closeprogramstate):
            self.gobuttonpress = gobuttonstate
            self.dummytext = 0
            
        def gobuttoninput(self):
            self.gobuttonpress = not gobuttonstate
        
#         #dummy function for testing modifying text in an open window
#         def dummygen(self):
#             self.dummytext += 1
            
            
    #make the button output object
    buttonanswer = Buttonoutput(gobuttonstate, closeprogramstate)    
            
    #for assigning data to the button output object
    def gobuttonpress():
        buttonanswer.gobuttoninput()
        
    #title for the widget
    title = 'Pilot standing widget'
        
    #Create an instance of Tkinter frame
    win= tk.Tk()

    #Set the geometry of Tkinter frame
    win.geometry("300x950")
    
    #set window color
    #win.configure(bg='light grey')
    
    #set the window title
    win.title(title)

    #import the background image
    background = tk.PhotoImage( file= "images/pilotrank.png")
    buttonimage = tk.PhotoImage(file = "images/button.png")
    
    #create canvas
    width = 300
    height = 950
    mycanvas = tk.Canvas(win, width = width, height = height)
    mycanvas.pack(fill = 'both', expand = True)
    
    #set image in canvas
    mycanvas.create_image(0,0, image = background, anchor = 'nw')
    
    #add a label
    textlines = '-------------------------------'
    fillcolor = 'green'
#     for index in range(len(finallist)):
#         if index > 7:
#             fillcolor = 'light gray'
#         mycanvas.create_text(width*2/16,25*index+140,text=finallist[index].name,
#                              font=("Arial 12 bold"),fill=fillcolor,anchor = 'nw')
#         mycanvas.create_text(width*2/16,25*index+152,text=textlines,
#                              font=("Arial 12"),fill='dark gray',anchor = 'nw')
#         mycanvas.create_text(width*12/16,25*index+140,text=finallist[index].pointtotal,
#                              font=("Arial 12 bold"),fill=fillcolor,anchor = 'nw')

    #add the button to the window
    button1 = tk.Button(win, image = buttonimage, borderwidth=0, text= "",width= 300, height = 136, command=
              lambda:[gobuttonpress(), makelabels(fillcolor)])
                #lambda:[gobuttonpress(), buttonanswer.dummygen(), makelabels(fillcolor)])
    button1window = mycanvas.create_window(width*8/16, 0, anchor = 'n', window = button1)

    #add the text to the window
    def makelabels(fillcolor):
        #get the final list data from the main script
        finallist = main.main()
        #overwrite the backound with a clean image
        mycanvas.create_image(0,0, image = background, anchor = 'nw')
        #make the pilot ranking text
        for index in range(len(finallist)):
            if index > 7:
                fillcolor = 'light gray'
            mycanvas.create_text(width*2/16,25*index+140,text=finallist[index].name,
                             font=("Arial 12 bold"),fill=fillcolor, anchor = 'nw')
            mycanvas.create_text(width*2/16,25*index+152,text=textlines,
                             font=("Arial 12"),fill='dark gray', anchor = 'nw')
            mycanvas.create_text(width*12/16,25*index+140,text=finallist[index].pointtotal,
                                 font=("Arial 12 bold"),fill=fillcolor,anchor = 'nw')

    win.mainloop()
    
    return buttonanswer.gobuttonpress

pilotrankwidget()