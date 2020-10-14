import sqlite3

cat yourfile.sql | sqlite3 newdatabase.db
conn = sqlite3.connect('newdatabase.db')

#althernate method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql_query.html