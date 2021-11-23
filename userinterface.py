import tkinter as tk


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
    win.geometry("1000x750")
    
    #set window color
    win.configure(bg='dark grey')
    
    #set the window title
    title = 'Street League automated race director'
    win.title(title)

    #Initialize a Label to display the User Input
    label = 'Press the big button to generate the next round'
    label= tk.Label(win, text=label, font=("Courier 20 bold"), background = "dark grey")
    label.pack()

    #Create a Button to validate Entry Widget
    tk.Button(win, text= "GO",width= 10, height= 5, font=("Courier 20 bold"), command=
                lambda:[gobuttonpress(), win.destroy()]).pack(padx = 20, pady = 100)
    tk.Button(win, text= "close program",width= 20, command=
                lambda:[closeprogram(), win.destroy()]).pack(pady = 150,)


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

def yesornowindow(label = '', title = ''):
    
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
    win.configure(bg='light grey')
    
    #set the window title
    win.title(title)

    #Initialize a Label to display the User Input
    label= tk.Label(win, text=label, font=("Courier 10 bold"), background = 'light grey')
    label.pack()

    #Create a Button to validate Entry Widget
    tk.Button(win, text= "Yes",width= 20, command=
              lambda:[clickyes(), win.destroy()]).pack(padx = 100, side = 'left')
    tk.Button(win, text= "No",width= 20, command=
              lambda:[clickno(), win.destroy()]).pack(padx = 100, side = 'right')
      
    win.mainloop()
    
    return buttonanswer.yesorno
    
#print(yesornowindow('enter name here'))