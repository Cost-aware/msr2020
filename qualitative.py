import pyodbc
import csv

cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()
cursor.execute("SELECT TOP 200 [Content]\
    FROM [sotorrent18_09].[dbo].[ReadabilityResult] where ReadabilityScore > 0.9")

rows = cursor.fetchall()

for row in rows :
    text = row[0]
    formatted = text.replace("&#xD;&#xA;", "\n\t")
    f = open("0.9.txt" , "a")
    f.write(formatted+'\n')
    f.write("---------------------------------\n\n")