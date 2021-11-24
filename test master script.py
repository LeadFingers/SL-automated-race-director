#import Leadstools as lead
import streetleagueheatmakerV2 as street
import userinterface as gui
import os

runvar = True

while(runvar):
    gobutton = True

    #exceldocname = street.maketxtfile()
    exceldocname = street.maketxtfile()

    #racedata = street.getxlsx(exceldocname)
    racedatatup = street.getxlsx(exceldocname)

    racedata = racedatatup[0]

    exceldocname = racedatatup[1]

    zerotime = street.checkfor0time(racedata, exceldocname)

    if zerotime == True:
        racersraw = street.makeracers(racedata)

        racersupdated = street.giveroundpoints(racersraw)

        racerssorted = street.firstsort(racersupdated[0])

        finallist = street.finalsort(racerssorted, racersupdated[1])

        newdataframe = street.makedataframe(finallist, racedata)

        street.exporttoxl(newdataframe, racedata, exceldocname)

    os.startfile(exceldocname)

    while(gobutton):
        loopvar = gui.biggobutton(gobutton, runvar)
        gobutton = loopvar[0]
        runvar = loopvar[1]
        if runvar == False:
            gobutton = False