# SL-automated-race-director
you need the most recent python as of 11/2021<br />you need the "pandas" plug-in<br />you need the "openpyxl" plug in<br /><br />How to use:<br />1-<br />enter the name of the excel doc that you are going to use to run the race<br />into "excel.doc.name.here.txt".  the file name MUST be the only thing<br />in this file.  EX:<br /><br />street.spec.race.xlsx<br /><br />no spaces, invisible lines, ANYTHING<br />probably best to use periods and dont put spaces in your file name.<br /><br /><br />2-<br />the excel file that will act as the program memory and input for the script<br />must be of the form of the template provided: "race.test.template.xlsx" <br /><br />round number	pilot names	point total	round time<br />1		LeadFingers	0		205.48<br />		Bumper		0		230.57<br />		...		...		...<br /><br /><br />DO NOT run the program with zero's in the "round time" column<br />DO NOT change the column names in row 1. if the program doesnt run check these<br />DO start with whatever points you want... havent tested negatives<br />DO feel free to add pilots whenever you want<br />DO manually change the pilot names, times, point totals as much as you want<br /><br /><br />3-<br />the script only reads the last sheet in the excel document. <br />you can make any changes you want to any sheet that isnt<br />the last one and it wont change anything. you can also delete<br />sheets if you want to role the race back.
3-
the script only reads the last sheet in the excel document. 
you can make any changes you want to any sheet that isnt
the last one and it wont change anything. you can also delete
sheets if you want to role the race back.
