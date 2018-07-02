
'''FrontEnd Database'''
import sqlite3

conn = sqlite3.connect('front_end_db.db')
records = [i for i in conn.cursor().execute('select * from table1')]
'''End of FrontEnd Database'''


'''BackEnd Database'''
from flask import Flask
import psycopg2

app = Flask(__name__)
@app.route('/syncdb')
def syncBackendDB():
    records = request.json()['data']
    
    conn = psycopg2.connect(database="task2",
                 user="back_end_db",
                 password="password",
                host="localhost", port="5432")
    for record in records:
        conn.cursor().execute("INSERT INTO table1 {0} VALUES {1}".format(tuple(record.keys()),tuple(record.values())))
    conn.commit()
    print "Records created successfully";
    conn.close()
if __name__ == '__main__':
    app.run()


#syncBackendDB()

