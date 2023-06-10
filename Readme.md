HashingExplainedto5yearold

When someone who isnt tech friendly asked me about google knowing all of our passwords because 
"they store them they have access to them" and that "any worker can just go in and see the passwords "
I created a very simple hashing algorithm to demonstrate how that wasnt the case, and how it can be stored in the database without anyone knowing it.

```rb
Hashing.py
#Each letter of a word is assigned a number, 
def hexchr(x):
    if(x == 'a'): return 1831;
    if(x == 'b'): return 2710;
    if(x == 'c'): return 483;
    if(x == 'd'): return 3692;
    if(x == 'e'): return 773;
    if(x == 'f'): return 3841;
    if(x == 'g'): return 327;
    if(x == 'h'): return 1419;
    if(x == 'i'): return 1059;
    if(x == 'j'): return 335;
    if(x == 'k'): return 3553;
    if(x == 'l'): return 1409;
    if(x == 'm'): return 2918;
    if(x == 'n'): return 4547;
    if(x == 'o'): return 695;
    if(x == 'p'): return 694;
    if(x == 'q'): return 4092;
    if(x == 'r'): return 2253;
    if(x == 's'): return 2317;
    if(x == 't'): return 3100;
    if(x == 'u'): return 3860;
    if(x == 'v'): return 3969;
    if(x == 'w'): return 354;
    if(x == 'x'): return 1439;
    if(x == 'y'): return 2276;
    if(x == 'z'): return 2240;
    if(x == '1'): return 483;
    if(x == '2'): return 3842;
    if(x == '3'): return 2311;
    if(x == '4'): return 817;
    if(x == '5'): return 3324;
    if(x == '6'): return 362;
    if(x == '7'): return 2479;
    if(x == '8'): return 4741;
    if(x == '9'): return 559;
    if(x == '0'): return 4207;
    if(x == 'ß'): return 1066;
    if(x == 'ä'): return 1785;
    if(x == 'ö'): return 1452;
    if(x == 'ü'): return 2376;
    if(x == '+'): return 4061;
    if(x == '-'): return 2685;
    if(x == '#'): return 2250;
    if(x == '@'): return 287;
    if(x == '!'): return 4188;
    if(x == '§'): return 1167;
    
   #that number then will be calculated with the rest of the numbers
    def hashpassword(password):
    l = len(password)
    res = 1
    for i in range(l):
        temp = hexchr(password[i]);
        res = res + pow(temp, 3) * temp * 34
    ln = len(str(res))
    return res;
```
Example :
```rb
main.py

print(hashed.hashpassword("test"))
#prints 7271985111664709
print(hashed.hashpassword("test1"))
# prints 7273835519420423
print(hashed.hashpassword("Iloveashley"))
# prints 11149784805523827
```
When the server stores your password, it stores it as this hashed password
and also checks and verifies it, as the hashed password
```rb
connsql.py

# the user user creates a new account with the password
#                   "Iloveashley"
# When user sets the passwords, the password is hashed and stored as
#                   11149784805523827
sqldb.checkpassword( idnum= 1 , currentpass="Iloveashley" )
# The server hashes the "Iloveashley", then sends the hash
#               11149784805523827
# to the database to check if it is the same and returns true or false
```
Hashing algorithms can get really compliacted and the more complex the algorithm is, the more reliable :

```rb
main.py

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
