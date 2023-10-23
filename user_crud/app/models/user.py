from flask import flash
# Config
from app.config.mysqlconnection import connectToMySQL

class User:
	def __init__(self, data):
		self.id = data["id"]
		self.first_name = data["first_name"]
		self.last_name = data["last_name"]
		self.email = data["email"]
		self.password = data["password"]
		self.created_at = data["created_at"]
		self.updated_at = data["updated_at"]
	
	@classmethod	
	def get_all(cls):
		""" Obtener todos los users. """
	
		query = """SELECT * FROM users;"""
		results = connectToMySQL("users").query_db(query)
		users: list = []
		
		for user in results:
			users.append(cls(user))
		return users
	
	@classmethod	
	def get_one(cls, data):
		query = """SELECT * FROM users WHERE id = %(id)s;"""
		return connectToMySQL("users").query_db(query, data)
	
	@classmethod	
	def delete(cls, data):
		query = """DELETE FROM users WHERE id = %(id)s;"""
		return connectToMySQL("users").query_db(query, data)
	
	@classmethod	
	def insert(cls, data):
	
		query = """INSERT INTO users(first_name, last_name, email, password) 
					VALUES 
						(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
		return connectToMySQL("users").query_db(query, data)

	@classmethod	
	def update(cls, data):
	
		query = """UPDATE users SET 
				first_name = %(first_name)s,
				last_name = %(last_name)s,
				email = %(email)s,
				password = %(password)s WHERE id = %(id)s;"""
		return connectToMySQL("users").query_db(query, data)