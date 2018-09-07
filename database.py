import psycopg2

class DatabaseConnection:
	def __init__(self):
		connection_credentials = """
				dbname='adminuser' user='adminuser' password='newpassword'
	            host='localhost' port='5432'
				"""
		try:
			self.connection = psycopg2.connect(connection_credentials)
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
			print('\n\nConnected to Database\n\n')
		except Exception as e:
			print(e.message)
			print('Failed to connect to db')


	def create_user(self, first_name, last_name, age, created_at):
		insert_user_command = """
        INSERT INTO vip_user (first_name, last_name, age, created_at) 
        VALUES ('{}', '{}', '{}', '{}');
        """.format(first_name, last_name, age, created_at)
		print(insert_user_command)
		self.cursor.execute(insert_user_command)
		count = self.cursor.rowcount
		return count


	def get_all_users(self):
		get_user_command = """
		SELECT * FROM vip_user;
		"""
		self.cursor.execute(get_user_command)
		users = self.cursor.fetchall()
		return users

	def fetch_user_by_username(self, username):
		get_user_command = """
		SELECT * FROM vip_user WHERE first_name= '{}';
		""".format(username)

		self.cursor.execute(get_user_command)
		user = self.cursor.fetchone()
		return user