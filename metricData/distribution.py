import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pyodbc


cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM [finalCodeResult]")

rows = cursor.fetchall()
lst = []

# for row in rows:
#     lst.append(row[4])

# sns.kdeplot(lst)
# plt.legend()
# plt.show()

####################################################################

lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []
lst8 = []
lst9 = []
lst10 = []
lst11 = []
lst12 = []
lst13 = []
lst14 = []
lst15 = []
lst16 = []
lst17 = []
lst18 = []
lst19 = []
lst20 = []

for row in rows:
    lst1.append(row[4])
    lst2.append(row[5])
    lst3.append(row[6])
    lst4.append(row[7])
    lst5.append(row[8])
    lst6.append(row[9])
    lst7.append(row[10])
    lst8.append(row[11])
    lst9.append(row[12])
    lst10.append(row[13])
    lst11.append(row[14])
    lst12.append(row[15])
    lst13.append(row[16])
    lst14.append(row[17])
    lst15.append(row[18])
    lst16.append(row[19])
    lst17.append(row[20])
    lst18.append(row[21])
    lst19.append(row[22])
    lst20.append(row[23])

lst.append(lst1)
lst.append(lst2)
lst.append(lst3)
lst.append(lst4)
lst.append(lst5)
lst.append(lst6)
lst.append(lst7)
lst.append(lst8)
lst.append(lst9)
lst.append(lst10)
lst.append(lst11)
lst.append(lst12)
lst.append(lst13)
lst.append(lst14)
lst.append(lst15)
lst.append(lst16)
lst.append(lst17)
lst.append(lst18)
lst.append(lst19)
lst.append(lst20)


print("done reading result")

i = 1
for ls in lst:
    f = open(str(i) + ".txt" , "a")
    f.write("max :  "+ str(np.amax(ls)) + '\n')
    f.write("min : "  + str(np.amin(ls))+ '\n')
    f.write("mean : " +str(np.mean(ls))+ '\n')
    f.write("var : " + str(np.var(ls))+ '\n')
    i += 1
print("DONE!")
