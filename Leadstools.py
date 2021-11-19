import pandas as pd
import openpyxl as pxl

#get the data from the spreadsheet and return it as a dataframe. also handles improperly formatted text
#by trying to add the extension for you and if that fales forces you to make a new file name
#using the maketxtfile() function
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
    return racedata


#this function either reads or creats a txt document and returns whatever text is in there in a string
#if correction is True it forces you to overwerite your text document with something new
#this is to stop the getxlsx() function from throwing errors
def maketxtfile(correction = False):  
    try:
        textfile = open('excel.doc.name.here.txt', 'x')
        
        exceldocname = input('enter the name of your excel document: ')
        
        with textfile as textfile:
            textfile.write(exceldocname)
        print('I made the txt file for you and put in your excel doc name')
        textfile.close()
    except:
        textfile = open('excel.doc.name.here.txt', 'r+')
        
        exceldocname = textfile.read()
        textfile.close()
        
        if exceldocname == '' or correction == True:
            textfile = open('excel.doc.name.here.txt', 'w')
            exceldocname = input('enter the name of your excel document: ')
            
            with textfile as textfile:
                textfile.write(exceldocname)
        print('the file was already there')
    
    print(exceldocname)
    return exceldocname

getxlsx('thewrongname')

########### This has been added to "streetleagueheatmakerV2"
# #this function checks if there are times entered for the 'round times' and asks the user if they want to
# #keep going or kill the script. running the script with no pilot times breaks things
# def checkfor0time(racedata):
#     
#     racertimelist = []
#     racertimes = True
#     missingtimelist = []
#     for row in range(len(racedata)):
#         if racedata.iloc[row]['round time'] == 0:
#             racertimes = False
#             missingtimelist.append(racedata.iloc[row]['pilot name'])
#     
#     if racertimes == False:
#         answer = ''
#         while answer !='y' or answer !='n': 
#             print('It looks like you forgot to enter times for', missingtimelist)
#             answer = input('having racer times of 0 can break the script, do you want to continue? y/n: ')
#             
#             if answer == 'n':
#                 print('go fix your race times')
#                 quit()
#             if answer == 'y':
#                 return

