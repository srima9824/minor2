#!"C:\Program Files\Python 3.5\python.exe"
import cgi,cgitb
import cx_Oracle
from abc import ABC, abstractmethod 
print("Content-Type: text/html \n\n")                      
 
class Login:
    def __init__(self):
        self.name = ""
        self.password = ""
    
    def getDetails(self):
        cgitb.enable() #for debugging
        form = cgi.FieldStorage()
        self.name = form.getvalue('name')
        self.password = form.getvalue('password')

class UserLogin(Login):
    def validateUser(self):
        try:
            result = False
            conn = cx_Oracle.connect(user = 'ADMIN1',password = 'admin1',dsn = 'xe')
            cur=conn.cursor()
            #print(self.name)
            #print(self.password)
            #cur.execute("""select * from USER_REG where NAME = :param1 and PASSWORD = :param2""",(self.name, self.password))
            query = "select * from USER_REG where NAME = '%s' and PASSWORD = '%s'" % (self.name,self.password)
            cur.execute(query)
            result = cur.fetchall()
            #print(result)
            if cur.rowcount == 0:
                print('<html><body><p>User does not exist</p></body><html>')
            else:
                redirectURL = "http://localhost/minor2/yaatri/index.html"
                print('<html>')
                print('  <head>')
                print('   <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
                print('  </head>')
                print('</html>')
        except Exception as e:
            print('<html><body><p> %s </p></body></html>',str(e))
        finally:
            conn.commit()
            conn.close()
            
user = UserLogin()
user.getDetails()
user.validateUser()