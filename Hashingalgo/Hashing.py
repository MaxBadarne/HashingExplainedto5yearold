# just to be clear, this is NOT an actual hashing algorithm, far from it, 
# this was writen to simply demonstrate how hashing works
# Real hashing algorithms are far more complicated than this
def hashpassword(password):
    l = len(password)
    res = 1
    for i in range(l):
        temp = hexchr(password[i]);
        res = res + pow(temp, 3) * temp * 34
    ln = len(str(res))

    return res;
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
    else:
        return False;
    
# I removed some other calculations and if statements in order to make it suitable for a 5 year old to understand
