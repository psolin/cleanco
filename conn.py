import sqlite3

def all_terms():
	conn = sqlite3.connect('data/terms.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	c.execute('SELECT * FROM term ORDER BY description;')
	rows = c.fetchall()
	return(rows)

def country_term(term):
	conn = sqlite3.connect('data/terms.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	c.execute('SELECT country FROM countryterm WHERE term = ?', (term,))
	rows = list(c)
	return(rows)

def type_term(term):
	conn = sqlite3.connect('data/terms.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()
	c.execute('SELECT type FROM typeterm WHERE term = ?', (term,))
	rows = list(c)
	return(rows)