import pyodbc
import numpy as np

cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()

cursor.execute("select AvgIdentifier, AvgLineLength, AvgAccolade, MaxLineLength,MaxIdentifierLength , AvgComment, LineCount, MaxIndentation ,AvgBlankLine , AngIndentation , AvgArithmatic from finalCodeResult where BlockId in (SELECT BlockId \
  FROM [sotorrent18_09].[dbo].[ReadabilityResult] where ReadabilityScore > 0.5)")

rows = cursor.fetchall()

AvgIdentifier = []
AvgLineLength = []
AvgAccolade = []
MaxLineLength= []
MaxIdentifierLength = []
AvgComment = []
LineCount = []
MaxIndentation = []
AvgBlankLine = []
AngIndentation =[]
AvgArithmatic =[]


for row in rows:
    AvgIdentifier.append(row[0])
    AvgLineLength.append(row[1])
    # AvgAccolade.append(row[2])
    MaxLineLength.append(row[3])
    MaxIdentifierLength.append(row[4])
    AvgComment.append(row[5])
    LineCount.append(row[6])
    # MaxIndentation.append(row[7])
    AvgBlankLine.append(row[8])
    AngIndentation.append(row[9])
    AvgArithmatic.append(row[10])


print("AvgIdentifier " +  str(np.mean(AvgIdentifier)))
print("AvgLineLength " +  str(np.mean(AvgLineLength)))
# print("AvgAccolade " +  str(np.mean(AvgAccolade)))
print("MaxLineLength " +  str(np.mean(MaxLineLength)))
print("MaxIdentifierLength " +  str(np.mean(MaxIdentifierLength)))
print("AvgComment "  +  str(np.mean(AvgComment)))
print("Linecount "  +  str(np.mean(LineCount)))
# print("MaxIndentation "  +  str(np.mean(MaxIndentation)))
print("AvgBlankLine "  +  str(np.mean(AvgBlankLine)))
print("AngIndentation "  +  str(np.mean(AngIndentation)))
print("AvgArithmatic "  +  str(np.mean(AvgArithmatic)))

print("\n\n")

print("AvgIdentifier " +  str(np.std(AvgIdentifier)))
print("AvgLineLength " +  str(np.std(AvgLineLength)))
# print("AvgAccolade " +  str(np.mean(AvgAccolade)))
print("MaxLineLength " +  str(np.std(MaxLineLength)))
print("MaxIdentifierLength " +  str(np.std(MaxIdentifierLength)))
print("AvgComment "  +  str(np.std(AvgComment)))
print("Linecount "  +  str(np.std(LineCount)))
# print("MaxIndentation "  +  str(np.mean(MaxIndentation)))
print("AvgBlankLine "  +  str(np.std(AvgBlankLine)))
print("AngIndentation "  +  str(np.std(AngIndentation)))
print("AvgArithmatic "  +  str(np.std(AvgArithmatic)))