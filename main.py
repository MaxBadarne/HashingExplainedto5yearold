import Hashingalgo.Hashing as hashed
import Sql.connsql as sqldb
import hashlib

print(hashed.hashpassword("test"))
#prints 7271985111664709
print(hashed.hashpassword("test1"))
# prints 7273835519420423
print(hashed.hashpassword("Iloveashley"))
# prints 11149784805523827

# the user user creates a new account with the password
#                   "Iloveashley"
# When user sets the passwords, the password is hashed and stored as
#                   11149784805523827
sqldb.checkpassword( idnum= 1 , currentpass="Iloveashley" )
# The server hashes the "Iloveashley", then sends the hash
#               11149784805523827
# to the database to check if it is the same and returns true or false


