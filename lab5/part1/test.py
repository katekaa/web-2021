import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)

c=db.cursor()
c.execute("INSERT INTO stations (name, year, line) VALUES (%s, %s, %s);", ('Семеновская', '1944', 3))
c.execute("SELECT * FROM stations ")
db.commit()
c.close()

