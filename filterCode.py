import pyodbc 
import csv
import re

cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server=.;"
                        "Database=sotorrent18_09;"
                        "Trusted_Connection=yes;", autocommit=False)

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM [NonEditedCodeHistory]")


def contain_keyword(code): #works
        words = [line.strip() for line in open('java_keywords.txt')]
        pattern = re.compile(r"\W+")
        word_count = 0
        line_fragments = pattern.split(code)
        
        for word in words:
            word_count += line_fragments.count(word)
        if word_count > 0:
            return True
        else:
            return False

rows = cursor.fetchall()
line  = 0 

javaBlockId = []
markDownBlockId = []



# with open('code_mixed_extended_final.csv', mode='w', encoding = "utf8" ) as employee_file:
    # java_writer = csv.writer(employee_file, delimiter='~', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # with open('markdown_mixed_extended_final.csv', mode='w', encoding = "utf8" ) as employee_file:
        # markdown_writer = csv.writer(employee_file, delimiter='~', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for w in rows:
    code = w[4]
    line_count = w[3]
    print ("reading line " , line)

    formatted_code = code.replace("&#xD;&#xA;", "\n\t")

    if line_count > 1:
        if formatted_code.count(";") > 0:
            # java_writer.writerow([w[1],code])
            # javaBlockId.append(w[1])
            cursor.execute("INSERT INTO [FilterNonEditedCodeHistory](RootBlockId , BlockId , CreationDate , LineCount , Content) VALUES(?, ?, ?, ?, ?)" , (w[0] , w[1] , w[2] , w[3] , w[4]))
        elif formatted_code.count("{") > 0 and formatted_code.count("(") > 1:
            # java_writer.writerow([w[1],code])
            cursor.execute("INSERT INTO [FilterNonEditedCodeHistory](RootBlockId , BlockId , CreationDate , LineCount , Content) VALUES(?, ?, ?, ?, ?)" , (w[0] , w[1] , w[2] , w[3] , w[4]))
            # javaBlockId.append(w[1])
        elif formatted_code.count("class") > 0 or formatted_code.count("for(") > 0 or formatted_code.count("java.") > 0 or formatted_code.count("private") >0 or formatted_code.count("public") > 0 or formatted_code.count("if(") > 0 or formatted_code.count("while(") > 0 :
            # java_writer.writerow([w[1],code])
            cursor.execute("INSERT INTO [FilterNonEditedCodeHistory](RootBlockId , BlockId , CreationDate , LineCount , Content) VALUES(?, ?, ?, ?, ?)" , (w[0] , w[1] , w[2] , w[3] , w[4]))
            # javaBlockId.append(w[1])
        else :
            markDownBlockId.append(w[1])
            # markdown_writer.writerow([code])
            
    else:
        if formatted_code.count(";") > 0:
            # java_writer.writerow([code])
            cursor.execute("INSERT INTO [FilterNonEditedCodeHistory](RootBlockId , BlockId , CreationDate , LineCount , Content) VALUES(?, ?, ?, ?, ?)" , (w[0] , w[1] , w[2] , w[3] , w[4]))
            # javaBlockId.append(w[1])
        elif len(re.findall(r'[a-zA-Z]' , formatted_code)) > 3 and formatted_code.count("(") > 0:
            # java_writer.writerow([code])
            cursor.execute("INSERT INTO [FilterNonEditedCodeHistory](RootBlockId , BlockId , CreationDate , LineCount , Content) VALUES(?, ?, ?, ?, ?)" , (w[0] , w[1] , w[2] , w[3] , w[4]))
            # javaBlockId.append(w[1])
        else:
            # markdown_writer.writerow([code])
            markDownBlockId.append(w[1])
            
    line += 1

cnxn.commit()

print("done!")
            # # filter markdown from java code : 
            # if formatted_code.count(";") > 0:
            #     java_writer.writerow([code])
            # elif line_count > 1 and formatted_code.count("(") > 0 and formatted_code.count("{") > 0:
            #     if contain_keyword(formatted_code) or formatted_code.count("java."):
            #         java_writer.writerow([code])
            #     else:
            #         markdown_writer.writerow([code])
            # elif line_count == 1 and formatted_code.count("(") > 0:
            #     if (len(re.findall(r'[a-zA-Z]' , formatted_code)) > 5):
            #         java_writer.writerow([code])
            #     else:
            #         markdown_writer.writerow([code])
            # else:
            #     markdown_writer.writerow([code])
            # line += 1