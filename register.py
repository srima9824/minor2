#!"C:\Program Files\Python 3.5\python.exe"
import cgi,cgitb
import cx_Oracle
print("Content-Type: text/html \n\n")                      
 
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('name')
password = form.getvalue('password')
contact = form.getvalue('contact')
nationality = form.getvalue('nationality')
conn = cx_Oracle.connect(user = 'ADMIN1',password = 'admin1',dsn = 'xe')
cur=conn.cursor()
cur.execute("select register.nextval from dual")
a = cur.fetchone()[0]
cur.execute("insert into USER_REG values(:1,:2,:3,:4,:5)",(a,name,password,contact,nationality))
conn.commit()
conn.close()

redirectURL = "http://localhost/minor2/yaatri/main.html"
print('<html>')
print('  <head>')
print('   <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')
