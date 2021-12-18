#import Leadstools as lead
import streetleagueheatmakerV2 as street
import userinterface as gui
import os
import tkinter as tk
import pandas as pd
import openpyxl as pxl

# runvar = True
# 
# #initail variables for persistant scoreboard
# gobuttonstate = True
# closeprogramstate = True

# while(runvar):
def main():
#     gobutton = True

    #exceldocname = street.maketxtfile()
    exceldocname = street.maketxtfile()

    #racedata = street.getxlsx(exceldocname)
    racedatatup = street.getxlsx(exceldocname)

    racedata = racedatatup[0]

    exceldocname = racedatatup[1]

    zerotime = street.checkfor0time(racedata, exceldocname)
    
    sametime = street.checkforsametime(racedata, exceldocname)

    if zerotime == True and sametime == True:
    
        racersraw = street.makeracers(racedata)

        racersupdated = street.giveroundpoints(racersraw)

        racerssorted = street.firstsort(racersupdated[0])

        finallist = street.finalsort(racerssorted, racersupdated[1])
            
        newdataframe = street.makedataframe(finallist, racedata)
        
        try:
            street.exporttoxl(newdataframe, racedata, exceldocname)
            
        except PermissionError:
            street.exceldocisopen() 
            
        
        
    os.startfile(exceldocname)

    return finallist

#back to old master script
#     while(gobutton):
#         #loopvar = gui.biggobutton(gobutton, runvar)
#         #loopvar = gui.pilotrankwidget(finallist = finallist)
#         gobutton = loopvar[0]
#         runvar = loopvar[1]
#         if runvar == False:
#             gobutton = False
