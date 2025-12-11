#task 1

import sqlite3

with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Jadval yaratamiz
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    ''')


#task 2

import sqlite3

with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    data = [
            ('Benjamin Sisko',	'Human',	40),
            ('Jadzia Dax',	'Trill',	300),
            ('Kira Nerys',	'Bajoran',	29)]

    cursor.executemany('INSERT INTO Roster VALUES(?,?,?)',data)



#task 3

import sqlite3

with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''UPDATE Roster
                   SET Name = 'Ezri Dax'
                   WHERE Name = 'Jadzia Dax'
                   ''')


#task 4
import sqlite3

with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''
                   SELECT Name, Age FROM Roster
                   WHERE Species = 'Bajoran'
                   ''')
    
    result = cursor.fetchall()
    for row in result:
        print(result)
    
