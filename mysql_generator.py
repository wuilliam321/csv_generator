import mysql.connector
import csv
from faker import Faker  # pip install Faker
fake = Faker()

cnx = mysql.connector.connect(user='root', password='root',
                              host='0.0.0.0',
                              port='3307',
                              database='tests')

query = []
# cedulas = []
with open('cedulas.csv', newline='') as cedulasfile:
    reader = csv.reader(cedulasfile)
    for row in reader:
        query.append("('ci-uy-%s', '%s')" % (row[0], fake.first_name()))

cursor = cnx.cursor()
add_destinatario = ("INSERT INTO destinatarios (id_uruguay, name) VALUES %s" % ','.join(query))
cursor.execute(add_destinatario)

cnx.commit()
cursor.close() 

cnx.close()