HashingExplainedto5yearold

When someone who isnt tech friendly asked me about google knowing all of our passwords because 
"they store them they have access to them" and that "any worker can just go in and see the passwords "
I created a very simple hashing algorithm to demonstrate how that wasnt the case, and how it can be stored in the database without anyone knowing it.

```rb
main.py
import Hashingalgo.Hashing as hashed
#import Sql.connsql as sqldb
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
#sqldb.checkpassword( idnum= 1 , currentpass="Iloveashley" )
# The server hashes the "Iloveashley", then sends the hash
#               11149784805523827
# to the database to check if it is the same and returns true or false


# Hashes get more and more complicated, adding new steps to the hasing algorithm
# taking the hashed number and turning into a hexadedecimal would be a good start
# *Using a real life but outdated hashing algorthm from the hashlib*
hashedlevel1 = hash("test")
print(hashedlevel1)
# prints            -69210052664837847
hashedlevel2 = hex(hash(hashedlevel1))
print(hashedlevel2)
# prints            0x2d9d101740746680
hashedlevel3 = hash(hashedlevel2.split("x")[1])
print(hashedlevel3)
#prints             4252262274784329667

# as we can see by adding a few steps, the password "test" was converted to 4252262274784329667
# if we add a few more complex steps to this, it would take some time for a good mathematician to figure out the hash
# Hashes are not made to be "reversed", from 4252262274784329667 we shouldnt be able to get "test"
```
