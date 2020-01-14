import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pyodbc
import csv
from collections import defaultdict



cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()
# cursor.execute("SELECT [AnswerScore], BlockId, ReadabilityScore FROM [sotorrent18_09].[dbo].[RootScore] join [ReadabilityResultNonEdited] on RootBlockId = [BlockVersionRootPostBlockVersionId] order by AnswerScore desc ")

# rows = cursor.fetchall()


cursor.execute("select RootBlockId , s , AnswerScore from [sotorrent18_09].[dbo].[RootScore] join  (select RootBlockId , count (RootBlockId) as s from ReadabilityResult group by RootBlockId) as t on RootBlockId = BlockVersionRootPostBlockVersionId")

rows2 = cursor.fetchall()
two = []
three = []
four = []
five = []
six = []
sevel = []
eight  =[] 
nine = []
ten = []


############## dont delete this part #####################
# for row in rows:
#     editlst.append(round(row[2] , 2))
#     scorelst.append(row[0])

for r in rows2 :
    if r[1] == 2:
        two.append(r[2])
    if r[1] == 3:
        three.append(r[2])
    if r[1] == 4:
        four.append(r[2])
    if r[1] == 5:
        five.append(r[2])
    if r[1] == 6:
        six.append(r[2])
    if r[1] == 7:
        sevel.append(r[2])
    if r[1] == 8:
        eight.append(r[2])
    if r[1] == 9:
        nine.append(r[2])
    if r[1] >= 10:
        ten.append(r[2])


print(np.mean(two))
print(np.std(two))
print(np.mean(three))
print(np.std(three))

print(np.mean(four))
print(np.std(four))

print(np.mean(five))
print(np.std(five))
print(np.mean(six))
print(np.std(six))
print(np.mean(sevel))
print(np.std(sevel))
print(np.mean(eight))
print(np.std(eight))
print(np.mean(nine))
print(np.std(nine))
print(np.mean(ten))
print(np.std(ten))

mean = [3.102]
ss = [1,2,3,4,5,6,7,8,9,10]


mean.append(round(np.mean(two),3))

mean.append(round(np.mean(three),3))


mean.append(round(np.mean(four),3))


mean.append(round(np.mean(five),3))

mean.append(round(np.mean(six),3))

mean.append(round(np.mean(sevel),3))

mean.append(round(np.mean(eight),3))

mean.append(round(np.mean(nine),3))

mean.append(round(np.mean(ten),3))

plt.plot(ss , mean)
plt.xlabel("number of version for a block")
plt.ylabel("score of answer containing that block")
plt.show()


# data = [two ,three , four, five , six , sevel , eight , nine , ten]

# plt.figure()


# plt.boxplot(two)
# plt.show()



# plt.scatter(editlst , scorelst)
# plt.xlabel("block version count")
# plt.ylabel("answer score")
# plt.show()

# print (np.max(lst))

# print (np.min(lst2))
# print (np.max(lst2))



# sns.kdeplot(lst)
# plt.legend()
# plt.show()

# resultDic = defaultdict(list)

# resultEdit = []
# resultLineCode = [] 
# for row in rows:
#     resultDic[row[0]].append(row[4])

# for row in rows:
#     lst = []
#     lst2 = []
#     if row[1] != row[0] :
#         edit_number = resultDic[row[0]].index(row[1])
#         if edit_number == 0 : 
#             edit_number = 1
        
        

# num_plots = 50

# colors = plt.cm.jet(np.linspace(0,1,num_plots))

# index = 0

# dif= []
# opcount = 0
# downcount = 0
# firstgood = 0
# secondgood = 0


# for i in resultDic:
#     lst = resultDic[i]
#     if lst[0] < lst[1] and lst[1] < lst[2]:
#         opcount += 1
#     if lst[0] > lst[1] and lst[1] > lst[2]:
#         downcount += 1
#     if lst[0] > lst[1] and lst[1] < lst[2]:
#         secondgood += 1
#     if lst[0] < lst[1] and lst[1] > lst[2]:
#         firstgood += 1
    

#     dif.append(abs(lst[0] - lst[1] - lst[2]))

# print (np.mean(dif))
# print (np.var(dif))
# print (opcount)
# print (downcount)
# print (firstgood)
# print (secondgood)


#     if (index >= 50 and index < 100):
#         lst = resultDic[i]
#         if lst[0] != lst[1]:
#             plt.plot([1,2] , [lst[0],lst[1]], color=colors[index-50])
#     index += 1
# plt.show()

   


print("DONE!!")




