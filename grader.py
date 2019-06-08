import psycopg2
from config import config
def connect():
	conn = None
	try:
		params = config()
		print("Connecting to the PostgreSQL DB")
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		print("PostgreSQL DB version:")
		cur.execute("Select version()")
		db_version = cur.fetchone()
		print(db_version)
		cur.execute("Select value from asu;");
		rows = cur.fetchall();
		total = cur.rowcount
		integer = 0
		for row in rows:
			r = list(row)
			if isinstance(r[0],int):
				print(r[0])
				integer+=1
		grade = integer / total * 100
		print(grade)

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print("Database connection closed.")

if __name__ == '__main__':
	connect()
