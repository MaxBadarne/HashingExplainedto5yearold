#This is the sql connection class, here a few methods are gonna be built, methods that belong to the sql database
#connect myssql
# This was created to simply demonstrate how passwords would use a hashing
# algorithm and then store the password safely in a database, and how the password can be verified 
import pymssql     # I used microsoft sql database here, but you settings can be easly changed to fit the type of database youre using 
import Hashingalgo.Hashing


#change the database settings here
host= "changeme"
user= "changeme"
password= "changeme"
db= "changeme"


conn = pymssql.connect(server=host, user=user, password=password, database=db)

#get id
def getlastid():
	getidquery = """SELECT ID , LAST_VALUE (ID) OVER (
		ORDER BY ID
		RANGE BETWEEN UNBOUNDED PRECEDING AND 
		UNBOUNDED FOLLOWING
	    ) FROM dbo.Users"""
	idqsl = conn.cursor()
	idqsl.execute(getidquery)
	idtupel = idqsl.fetchone()
	lastid = idtupel[1]
	return lastid
#ask for user name and password and puts them in the database
def createuser():
	id = getlastid() +1
	name = input("put a new name")
	passwordb4hash = input("input password retard")
	password = Hashingalgo.Hashing.hashpassword(passwordb4hash)
	insertquery ="INSERT INTO [dbo].[Users] " + "([ID] ,[Name] ,[Password]) " + "VALUES ( "+ str(id) + """,'""" + name + """','""" + str(password) + "')"
	insertuser = conn.cursor()
	insertuser.execute(insertquery)														
	print(insertquery)  #debug
	
#verify password  {return true of false}
def checkpassword( idnum , currentpass ):			    #herechange
	query = "select Password from Users where ID = "+str(idnum)
	row = conn.cursor()
	row.execute(query)
	idtupel = row.fetchone()
	actualpassword = idtupel[0]
	currentpasshashed = Hashingalgo.Hashing.hashpassword(currentpass)
	currentpasshashed = str(currentpasshashed)
	print(actualpassword)     #debug
	print(currentpasshashed)	#debug
	if(actualpassword == currentpasshashed): return True;
	else: return False;
	
print(checkpassword(2, "example"))

conn.commit()
conn.close()
