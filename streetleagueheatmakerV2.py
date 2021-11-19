import pandas as pd
import openpyxl as pxl
import Leadstools as lead
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


#this function checks if there are times entered for the 'round times' and asks the user if they want to
#keep going or kill the script. running the script with no pilot times breaks things
def checkfor0time(racedata):
    
    racertimelist = []
    racertimes = True
    missingtimelist = []
    for row in range(len(racedata)):
        if racedata.iloc[row]['round time'] == 0:
            racertimes = False
            missingtimelist.append(racedata.iloc[row]['pilot name'])
    
    if racertimes == False:
        answer = ''
        while answer !='y' or answer !='n': 
            print('It looks like you forgot to enter times for', missingtimelist)
            answer = input('having racer times of 0 can break the script, do you want to continue? y/n: ')
            
            if answer == 'n':
                print('go fix your race times')
                quit()
            if answer == 'y':
                return

def maketxtfile():  
    try:
        textfile = open('excel.doc.name.here.txt', 'x')       
        exceldocname = input('enter the name of your excel document: ')       
        with textfile as textfile:
            textfile.write(exceldocname)
        print('I made the txt file for you and put in your excel doc name')
    except:
        textfile = open('excel.doc.name.here.txt', 'r+')     
        exceldocname = textfile.read()        
        if exceldocname == '':
            exceldocname = input('enter the name of your excel document: ')         
            with textfile as textfile:
                textfile.write(exceldocname)
        print('the file was already there')
    print(exceldocname)
    return exceldocname
#this function either reads or creats a txt document and returns whatever text is in there in a string
#if correction is True it forces you to overwerite your text document with something new
#this is to stop the getxlsx() function from throwing errors
def maketxtfile(correction = False):  
    try:
        textfile = open('excel.doc.name.here.txt', 'x')
        
        #old method
        #exceldocname = input('enter the name of your excel document: ')
        
        #new method
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        exceldocname = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        #exceldocname = lead.select_file()
        
        with textfile as textfile:
            textfile.write(exceldocname)
        print('I made the txt file for you and put in your excel doc name')
        textfile.close()
    except FileExistsError:
        textfile = open('excel.doc.name.here.txt', 'r+')
        
        exceldocname = textfile.read()
        textfile.close()
        
        if exceldocname == '' or correction == True:
            textfile = open('excel.doc.name.here.txt', 'w')
            #exceldocname = input('enter the name of your excel document: ')
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            exceldocname = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            #exceldocname = lead.select_file()
            
            with textfile as textfile:
                textfile.write(exceldocname)
            print('the file was already there')
            
    except:
        print('File not found')
        self.maketxtfile(False)
    
    print(exceldocname)
    return exceldocname

# def maketxtfiledialog(correction = False):
#     try:
#         textfile = open('excel.doc.name.here.txt', 'x')
#         
#         with textfile as textfile:
#             textfile.write(exceldocname)
#         print('I made the txt file for you and put in your excel doc name')
#         textfile.close()
#     except:
#         Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#         exceldocname = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#         print(filename)

# def getxlsx(spreadsheet): #get the data from the spreadsheet and return it as a dataframe
#     sheet = pd.ExcelFile(spreadsheet)
#     worksheet = len(sheet.sheet_names)-1
#     
#     racedata = pd.read_excel(spreadsheet, sheet_name = worksheet)
#     print(racedata)
#     print('length of the race data: ', len(racedata))
#     print('-----------------------------')
#     return racedata

def getxlsx(spreadsheet):
    loopvar = True
    easyfix = True 
    while loopvar == True:
        try:
            sheet = pd.ExcelFile(spreadsheet)
            loopvar = False
            easyfix = True
        except FileNotFoundError:
            if easyfix == False:
                loopvar = False
            if easyfix == True:
                spreadsheet += '.xlsx'
                easyfix = False
        except ValueError:
            spreadsheet = maketxtfile(True)
        finally:
            if easyfix == False and loopvar == False:
                print('that document ', spreadsheet, ' doesnt exist')
                spreadsheet = maketxtfile(True)
                loopvar = True
                easyfix = True
        
    worksheet = len(sheet.sheet_names)-1
    
    racedata = pd.read_excel(spreadsheet, sheet_name = worksheet)
    print(racedata)
    print('length of the race data: ', len(racedata))
    print('-----------------------------')
    return (racedata, spreadsheet)


class Racer(object): #a way to store the pilots time and points with their name
    def __init__(self, name, roundtime, pointtotal):
        self.name = name
        self.roundtime = roundtime
        self.pointround = 0
        self.pointtotal = pointtotal
        self.racerank = 0

    def givepointround(self, rank): #allows you to change the points the pilot earned
        self.pointround += rank

    def newrank(self): #updates the point total by adding it to the pilots rank
        self.pointtotal += self.pointround
    
def makeracers(racedata): # make all of the racer objects from the spreadsheet dataframe
                                                        # outputs a dictionary with indexes 0 -> num of racers -1
                                                        # the values are Racer class objects
    print('there are ', len(racedata), ' racers')
    racerdic = {}
    for row in range(len(racedata)):
        pilotname = racedata.iloc[row]['pilot name']
        pointtotal = racedata.iloc[row]['point total']
        roundtime = racedata.iloc[row]['round time']
        racerdic[row] = Racer(pilotname, roundtime, pointtotal)
        print(racerdic[row].name, racerdic[row].roundtime, racerdic[row].pointtotal)
    print('--------------------------------')
    return racerdic

def giveroundpoints(racersraw): #takes all the raw racer data (dic) from the last round and
# asigns them points and updates the pilot object. returns the updated racers in
#the order they finished the last round in index [0]. and 
    workingdic = {}
    workinglist = []
    rankeddic = {}

    for row in range(len(racersraw)):
        #make racer dic with index = roundtime
        workingdic[racersraw[row].roundtime] = racersraw[row]
        #make a list of the index's 
        workinglist.append(racersraw[row].roundtime)
        
    #sort the list of inexes
    workinglist.sort()
    print(workinglist)

    for index in range(len(workinglist)):

        rank = index+1
        #update the Racer object with points for the round
        workingdic[workinglist[index]].givepointround(rank)
        #update the point total with the points from the round
        workingdic[workinglist[index]].newrank()
        #put the racers in order into the new dictionary
        rankeddic[index] = workingdic[workinglist[index]]

    for row in range(len(rankeddic)):
        print(rankeddic[row].name,rankeddic[row].roundtime,
              rankeddic[row].pointround, rankeddic[row].pointtotal)
    print('-----------------------------------------')

    return (rankeddic, workingdic)

def firstsort(racersupdated): #this function will sort the racers by their point
    #totals and deal with point ties by happenstance and magic. probably has to do
    #with them starting in the order of best finish in the last round
    unsortedlist = []   
    for pilot in racersupdated:
        tinylist = []
        tinylist.append(racersupdated[pilot].pointtotal)
        tinylist.append(racersupdated[pilot].roundtime)
        tinylist.append(racersupdated[pilot].name)
        unsortedlist.append(tinylist)  
    #print(unsortedlist)
    firstsortlist = sorted(unsortedlist, key = lambda x: x[0])
    #print(firstsortlist)
    
    return firstsortlist

def finalsort(sortedlist, sorteddic):#this function takes a list of lists [[points, last round time, pilot name], ...] 
#that is correctly ordered in the pilots race ranking from 1st [0] to last and a dictionary
#containing the pilot objects indexed by their last round time and returns
# a list of pilot objects in the correct ranking order

    sortedpilotlist = []
    for index1 in range(len(sortedlist)):
        sortedpilotlist.append(sorteddic[sortedlist[index1][1]])
        print(sortedpilotlist[index1].name, sortedpilotlist[index1].pointtotal, sortedpilotlist[index1].roundtime)
    return sortedpilotlist
    
def makedataframe(finallist, testdoc):
    data = []
    columns = ['round number','pilot name', 'point total', 'round time']

    for index in range(len(finallist)):
        tinylist = [str(testdoc.at[0,'round number'] + 1), finallist[index].name, finallist[index].pointtotal, 0]
        data.append(tinylist)

    newdataframe = pd.DataFrame(data, columns = columns)
    print(newdataframe)

    return newdataframe
        
def exporttoxl(newdataframe, testdoc, spreadsheetfile):
    
    newround = 'round number ' + str(testdoc.at[0,'round number'] + 1)
    
    #testdoc.to_excel(spreadsheetfile, 'round 1', index = False)
    
    excel_book = pxl.load_workbook(spreadsheetfile)
    with pd.ExcelWriter(spreadsheetfile, engine = 'openpyxl') as writer:
        writer.book = excel_book
        writer.sheets = {
            worksheet.title: worksheet
            for worksheet in excel_book.worksheets}
        newdataframe.to_excel(writer, newround, index = False)
        





