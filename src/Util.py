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
    parts = []
    prevpoint = 0
    i = 1
    print len(string)/hashsize
    # Seperate string into piecies for hashing
    while i is not (len(string)/hashsize) + 1:
        parts.append(string[prevpoint:hashsize*i])
        prevpoint = hashsize*i
        i += 1
    last = parts[-1]
    print last
    if last is not string[-hashsize:]:
        print "not done"
    return parts