#! /python34/python
import cgi, cgitb, mysql.connector, imp

# MYSQL CONFIG VARIABLES
host           = "localhost";
db             = "webair";
user           = "root";
passwd         = ""

def getConnection():
	conn = mysql.connector.connect(user=user,
								   password=passwd,
								   host=host,
								   database=db
)
	return conn