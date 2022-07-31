import psycopg2

connection = psycopg2.connect(database="sqlpoll")

cursor = connection.cursor()

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)