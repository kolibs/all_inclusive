from sqlalchemy import create_engine #

class Dict():
    def __init__(self):
        db = create_engine("sqlite:///mapping.db")
        connect = db.connect()
        query = connect.execute("select * from mapping")
        self.data = dict(query.cursor.fetchall())
        connect.close()
        db.dispose()
               
    def sort(self):
        return [ key for key in sorted(self.data)]
                 
    def get_inclusive(self, name):
        return self.data[name]
