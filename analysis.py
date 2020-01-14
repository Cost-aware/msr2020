import pyodbc
import csv
import math
import numpy as np
import calendar
import time

class RootBlock:
    def __init__(self, id):
        self.id = id 
        self.versionList = []

class VersionBlock:
    def __init__(self, id, lineCount, creationDate, score, index):
        self.id = id
        self.lineCount = lineCount
        self.creationDate = creationDate
        self.score = score
        self.index = index 

cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()
cursor.execute("select * from [sotorrent18_09].[dbo].[ReadabilityResult] ORDER BY RootBlockId desc , CreationDate asc")

rows = cursor.fetchall()
print ("got all the result score !")

blockList = {}
blockAdded = False

currentRoot = 0 

for row in rows:
    root = row[0]
    block = row[1]
    creation = row[2]
    linecount = row[3]
    score = row[4]
    if currentRoot != root:
       
        currentRoot = root
        rootBlock = RootBlock(root)
        
        indx = len(rootBlock.versionList)
        # print ("new root added ")
        blockV = VersionBlock(block, linecount, creation , score, indx)
        rootBlock.versionList.append(blockV)
        
        blockList[root] = rootBlock
    elif currentRoot == root:
        
        root = blockList[root]

        indx = len(root.versionList)
        # print ("new root added " , str(indx) , "  " , str(creation))
        blockV = VersionBlock(block, linecount, creation , score, indx)
        root.versionList.append(blockV)
print ("done creating data !")


############################ sample of bad edit 

for r in blockList:
    lst = blockList[r].versionList
    i = 1 
    # while i < len(lst):
    block0 = lst[0]
    block1 = lst[-1]
    if block1.score > 0:
        if block0.score > 0.9 and  block1.score < 0.1 and block0.lineCount > 8 and block1.lineCount > 8:
            print ("first block and edit block are : " , block0.id, "   ",block1.id)
        # i += 1



############################ getting data for decision tree alanysis 
# with open('analysis4.csv', mode='w', encoding = "utf8", newline = '' ) as f:
#     writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for r in blockList:
#         blocklst = blockList[r].versionList
#         i = 1
#         while i < len(blocklst):
#             blck0 = blocklst[i-1]
#             blck1 = blocklst[i]

#             if blck1.score > 0: 
#                 m = math.floor((blck1.creationDate - blck0.creationDate).seconds)/60
#                 minute = round(m , 2)
#                 re = ""
#                 if blck1.score > blck0.score:
#                     re = "good"
#                 elif blck1.score < blck0.score:
#                     re = "bad"
#                 writer.writerow([blck1.index, blck1.lineCount, blck0.lineCount-blck1.lineCount, minute , blck1.score ,re])
#             i += 1
#             print("new line added !")
#     print("done creating csv file")

######################### formatting data for statistical analysis 
# goodCount = 0
# badCount = 0
# goodList = []
# badList = []
# mehcount = 0

# f = open("editIndexAnalysis.txt", "a")
# for r in blockList:
#     lst = blockList[r].versionList
#     rt = lst[0]
#     i = 9
#     if i < len (lst):
#         blck = lst[i]
#         difScore = blck.score - rt.score
#         goodList.append(difScore)

# print(np.mean(goodList))
# print(np.std(goodList))
#         if difScore > 0:
#             goodCount += 1
#             goodList.append(difScore)
#         elif difScore < 0 :
#             badList.append(difScore)
#             badCount += 1
#         else:
#             mehcount += 1
# goodMean = np.mean(goodList)
# goodVar = np.var(goodList)

# badMean = np.mean(badList)
# badVar = np.var(badList)

# f.write("changes from root to 10th version \n")
# f.write("number of blocks with score more than root : " + str(goodCount) + '\n')
# f.write("mean and variance for higher scores : " + str(goodMean) + " " + str(goodVar) + '\n')
# f.write("number of blocks with score less than root : " + str(badCount) + '\n')
# f.write("mean and variance for lower scores : " + str(badMean) + " " + str(badVar) + '\n')
# f.write("meh : " + str(mehcount) + '\n')
# f.write("---------------------------------\n")

