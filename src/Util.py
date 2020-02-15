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
    return parts