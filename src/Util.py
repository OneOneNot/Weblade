# Writen by OneOneNot
# 14/2/2020

# User util
def get_log_uuid(log):
    uuid = log[:10]
    return uuid


def get_log_cookie(log):
    cookie = log[-10:]
    return cookie


def get_log_ip(log):
    ip = log[10:-10]
    return ip

# Server util
def redirect():
    print ""
    
# 15/2/2020

def webhash(string, hashsize):
    
    # Step 1 Seperate
    
    rem = len(string) % hashsize
    if rem is not 0:
        string += "0" * rem
    parts = []
    prevpoint = 0
    i = 1
    # Seperate string into piecies for hashing
    while i is not (len(string)/hashsize) + 1:
        parts.append(string[prevpoint:hashsize*i])
        prevpoint = hashsize*i
        i += 1
    
    # Step 2 Setup
    
    flist = []
    for part in parts:
        prt = part
        i = 0
        while i is not len(prt):
            chars = []
            chars.append(ord(prt[i]))
            j = 0
            while j is not hashsize:
                if j is not (len(chars) - 1):
                    chars.insert(j, chars[j] + chars[j + 1])
                else:
                    chars.insert(j, chars[j] + chars[0])
                flist.append(chars)
                j += 1
            i += 1
            
    # Step 3 Final hash
    
    finalhashlist = []
    i = 0
    # Step 3.1 Calculate
    while i is not hashsize:
        colsum = 0
        j = 0
        while j is not (len(string)/hashsize):
            colsum += flist[i][j]
            j += 1
        finalhashlist.append(colsum)
        i += 1
        
    # Step 3.2 Convert
    finalhash = ""
    for fhl in finalhashlist:
        finalhash += chr(fhl/256)
    print finalhashlist
    return finalhash