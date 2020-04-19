import sqlite3
import os.path

def create_connection():
  c = sqlite3.connect("terms.db")
  fd = open('terms.sql', 'r')
  script = fd.read()
  c.executescript(script)
  fd.close()
  print("db created")

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