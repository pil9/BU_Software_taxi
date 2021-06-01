import sqlite3
import pdb
def register_db(user_name, user_id, user_pw):
	con = sqlite3.connect("register.db", isolation_level=None)
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS register\
	(user_name TEXT, user_id TEXT PRIMARY KEY, user_pw TEXT)")
	# cur.execute("CREATE TABLE IF NOT EXISTS board\
	# (user_name TEXT, user_id TEXT, user_pw TEXT)")
	# (id_num INTEGER PRIMARY KEY, user_name TEXT, user_id TEXT, user_pw TEXT)")
	test_tuple = (user_name, user_id, user_pw)
	cur.execute("INSERT INTO 'register'(user_name, user_id, user_pw) VALUES(?,?,?)", test_tuple)
	con.commit()
	cur.close()
	con.close()

def login_db(user_id):
	con = sqlite3.connect("register.db", isolation_level=None)
	cur = con.cursor()
	# pdb.set_trace()
	exist_value = cur.execute("SELECT EXISTS(SELECT 1 FROM register WHERE user_id = ?)",(user_id,)).fetchone()[0]
	return exist_value
	# print(test)


def recruit_db(user_name, departure, destination, time):
	con = sqlite3.connect("register.db", isolation_level=None)
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS recruit\
	(user_name TEXT, departure TEXT, destination TEXT, closed TEXT)")
	# (id_num INTEGER PRIMARY KEY, user_name TEXT, user_id TEXT, user_pw TEXT)")
	row_tuple = (user_name, departure, destination, time)
	cur.execute("INSERT INTO 'recruit'(user_name, departure, destination, closed) VALUES(?,?,?,?)", row_tuple)
	con.commit()
	cur.close()
	con.close()

def declare_db(black_date, black_name, reason_reporting):
	con = sqlite3.connect("register.db", isolation_level=None)
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS declare\
	(black_date TEXT, black_name TEXT,reason_reporting TEXT)")
	# (id_num INTEGER PRIMARY KEY, user_name TEXT, user_id TEXT, user_pw TEXT)")
	test1_tuple = (black_date, black_name, reason_reporting)
	cur.execute("INSERT INTO 'recruit'(black_date, black_name,reason_reporting) VALUES(?,?,?)", test1_tuple)
	con.commit()
	cur.close()
	con.close()