from sqlalchemy import create_engine #

class Dict():
    def __init__(self):
        db = create_engine("sqlite:///mapping.db")
        connect = db.connect()
        query = connect.execute("select * from mapping")
        self.data = dict(query.cursor.fetchall())
        connect.close()
        db.dispose()
               
    def generate_html_dict(self):
        html = ""
        for key in sorted(self.data):
            html += "<a href=\"/web/{0}\">>{0}<a/><br />".format(key)
        return html
         
    def get_inclusive(self, name):
        return self.data[name]
