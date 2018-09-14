import os
import operator
import sqlite3



data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
files = os.listdir(data_path)

history_db = os.path.join(data_path, 'history')


c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall() 

defile = open("gg.txt","a+")



for t in results:
    line = ' '.join(str(x) for x in t)
    defile.write(line + '\n')
defile.close()
