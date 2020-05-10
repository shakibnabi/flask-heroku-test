import pymysql

class table:
    def __init__(self,table):
        host = "foxdosbd.com"
        user = "foxdosbd_skbforce142536"
        password = "0?qMBcSXS^Zi"
        db = "foxdosbd_apiCenter"
        self.table = table


        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def show(self):
        self.cur.execute("SELECT * FROM "+self.table)
        result = self.cur.fetchall()

        return result

    def showbyid(self, col, val):
        self.cur.execute("SELECT * FROM "+self.table+" WHERE email = %s AND password = %s", (val))
        result = self.cur.fetchone()

        return result

    def insert(self,val,cols,formate):
        self.cur.execute("INSERT INTO "+self.table+"("+cols+") VALUES ("+formate+")",(val))
        self.con.commit()
        return 'Worked'

    def update(self,val,cols,condition):
        # flrno = %s, unitno = %s
        self.cur.execute('UPDATE '+self.table+' SET '+cols+' WHERE '+condition,(val))
        self.con.commit()
        return 'Worked'

    def delete(self,val,condition):
        # flrno = %s, unitno = %s
        self.cur.execute('DELETE FROM '+self.table+' WHERE '+condition,(val))
        self.con.commit()
        return 'Worked'

