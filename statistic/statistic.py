import numpy as np 
import pandas as pd 
import pyodbc 
import csv
import matplotlib.pyplot as plt 
import csv2arff


# class Statistic():
#     def __init__(self , lst):
#         self.result = lst

#     def getMean(self):
#         return np.mean(self.result)
    
#     def getVariance(self):
#         return np.var(self.result)
    
#     def IQR (self):
#         d = {}
#         q75, q25 = np.percentile(self.result , [75 ,25])
#         iqr = q75 - q25
#         d['q1'] = q25
#         d['q3'] = q75
#         d['iqr'] = iqr
#         return d


###############################################################################
# cnxn = pyodbc.connect("Driver={SQL Server};"
#                         "Server=.;"
#                         "Database=sotorrent18_09;"
#                         "Trusted_Connection=yes;", autocommit=False)

# cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM [finalCodeResult]")

# rows = cursor.fetchall()


# with open('statistic4.csv', mode='w', encoding = "utf8", newline = '' ) as f:
#     writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for w in rows:
#         writer.writerow([w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10],w[11],w[12],w[13],w[14],w[15],w[16],w[17],w[18],w[19],w[20],w[21],w[22],w[23]])
##############################################################################

df = pd.read_csv("statistic4.csv") 

 # Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)
ax.set_title('avg arithmatic')
# Create the boxplot
bp = ax.boxplot(df.iloc[1], showfliers=True)

for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

plt.show()

###############################################################################

# df = pd.read_csv('statistic3.csv')

# lst = []
# with open("statistic2.csv", encoding = "utf8") as posts:
    # posts_reader = csv.reader(posts, delimiter=',')
#     for row in posts_reader:
#         if (len(row) != 0):
#             lst.append(row[0])

# print (len(lst))
# a , b , c = 0,0,0 
# d, e, f = 0 , 0 ,0

# for i in lst :
#     if int(i) >= 1 and int(i) < 5:
#         a += 1
#     elif int(i) >=5 and int(i) < 10:
#         b +=1
#     elif int(i) >= 10 and int(i) <50:
#         c += 1
#     elif int(i)>= 50 and int(i) < 100:
#         d += 1
#     elif int(i) >= 100 and int(i) < 500:
#         e += 1
#     else :
#         f += 1

# lst2 = [a,b,c,d,e,f]
# print(lst2)

# plt.hist(lst2)
# plt.show()
###########################################################################