import sqlite3

print("Creating database \'Task\'...")

conn = sqlite3.connect('Task')

print("Created database \'Task\' successfully...")

c = conn.cursor()

print("Creating table \'Movies\'...")

c.execute('''
          CREATE TABLE IF NOT EXISTS Movies
          (id INT PRIMARY KEY NOT NULL,
          name TEXT NOT NULL, 
          actor TEXT NOT NULL, 
          actress TEXT NOT NULL, 
          director TEXT NOT NULL, 
          year_of_release INT NOT NULL)
          ''')

print("Created table \'Movies\' successfully...")

print("Inserting data...")

c.execute('''INSERT INTO Movies
          VALUES(1,'The Last Year','Daniel','Ralki','Carlos',2019)''')

c.execute('''INSERT INTO Movies
          VALUES(2,'Curse','Marchel','Isabel','Eddy',2016)''')

c.execute('''INSERT INTO Movies
          VALUES(3,'My Dream','Shanky','Hobby','Lark',2020)''')

c.execute('''INSERT INTO Movies
          VALUES(4,'Infinity','Draken','Easlu','Eonal',2016)''')

print("Inserted data successfully...\n")

print("Fetching all rows with *.\n")

c.execute('''SELECT * FROM Movies''')

for row in c.fetchall():
    print("Movie Id: {0}, Movie Name: {1}, Movie Acror: {2}, Movie Actress: {3}, Movie Director: {4}, Year of release: {5}.".format(
        row[0], row[1], row[2], row[3], row[4], row[5]))

print("\nFetching movies id and names with where clause.\n")

c.execute("SELECT id,name FROM Movies WHERE actor='Shanky' or year_of_release=2016")

for row in c.fetchall():
    print("Movie Id: {0}, Movie Name: {1}.".format(row[0], row[1]))

conn.commit()
