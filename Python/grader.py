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
		cur.execute(open("submission.sql","r").read())
			
		cur.execute("Select value from asu1;")
		rows = cur.fetchall()
		submission = []
		result = []
		error = 0
		for row in rows:
			r = list(row)
			if isinstance(r[0],int):
				#print(r[0])
				submission.append(r[0])	
			else:
				error +=1
		cur.execute("Select value from asu;")
		rows = cur.fetchall()
		for row in rows:
			r = list(row)
			if isinstance(r[0],int):
				result.append(r[0])
				#print(r[0])
		grade = 10
		if len(result) - len(submission) != 0:
			grade = grade - (abs(len(result)-len(submission)))*0.1
		for i in range(len(result)):
			if result[i]!=submission[i]:
				error +=1
		grade -= error
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
