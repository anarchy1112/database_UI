import sqlite3


def connect():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY, date text, earnings integer, exercise text, '
                'study text, diet text, python text)')
    conn.commit()
    conn.close()

def insert(date, earnings, exercise, diet, study, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL, ?,?,?,?,?,?)" ,(date, earnings, exercise, diet, study, python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(date='', earnings='', exercise='', diet='', study='', python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR diet=? OR study=? OR python=?", (date, earnings, exercise, diet, study, python))
    rows = cur.fetchall()
    conn.close()
    return rows

# insert('20.01.2023', 3000, 'no', 'yes', 'no', 'yes')
# connect()
# print(view())
# delete(1)
# print(search(date='01.01.2023'))

