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