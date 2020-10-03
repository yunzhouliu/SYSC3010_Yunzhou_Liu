import sqlite3



dbconnect = sqlite3.connect("sensors.db");

dbconnect.row_factory = sqlite3.Row;

cursor = dbconnect.cursor();

cursor.execute('''create table sensors (sensorID integer, type text, zone text)''');

cursor.execute('''insert into sensors values (1,'door','kitchen')''');
cursor.execute('''insert into sensors values (2,'temperature','kitchen')''');
cursor.execute('''insert into sensors values (3,'door','garage')''');
cursor.execute('''insert into sensors values (4,'motion','garage')''');
cursor.execute('''insert into sensors values (5,'trmperature','garage')''');
dbconnect.commit();

cursor.execute("SELECT * FROM sensors where type = 'door'");

for row in cursor:
    
    print(row['sensorID'],row['type'],row['zone']);


cursor.execute("SELECT * FROM sensors where zone = 'kitchen'");

for row in cursor:
    
    print(row['sensorID'],row['type'],row['zone']);

dbconnect.close();
