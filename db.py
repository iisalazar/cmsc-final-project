import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"

MYSQL_PASS = "UPlangmalakaz"

MYSQL_DB = "splitwise_clone"


db = mysql.connector.connect(
    host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASS, database=MYSQL_DB
)
