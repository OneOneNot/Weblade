# Writen by OneOneNot
# 14/2/2020

import socket
import Util


class Client():
    # This class handles client data
    def __init__(self, uuid):
        self.ip = "0.0.0.0"
        self.port = 0000
        self.cookie = ""
        self.uuid = uuid
        
    # This function is saving in a file the user data   
    def save_client(self, logfile):
        sep = "\n"
        client = self.uuid + self.ip + self.cookie
        f = open(logfile, "r")
        prlog = f.read()
        f.close()
        f = open(logfile, "w")
        f.write(prlog + sep + client)
        
        
    def load_client_by_uuid(self, logfile, uuid):
        found = False
        f = open(logfile, "r")
        fuuid = Util.get_log_uuid(f.readline())
        while not found:
            if fuuid is uuid:
                found = True
            else:
                fuuid = Util.get_log_uuid(f.readline())
        
        
    def load_client_by_cookie(self, logfile, cookie):
        found = False
        f = open(logfile, "r")
        fcookie = Util.get_log_cookie(f.readline())
        while not found:
            if fcookie is cookie:
                found = True
            else:
                fcookie = Util.get_log_cookie(f.readline())
    
    
    def get_user_data(self):
        print ""
        
        
    def delete_user(self):
        print ""


class Server():
    
    def __init__(self, ip, p):
        self.host = ip
        self.port = p
        
    
    def start(self):
        try:
            self.s = socket.socket()
        except Exception as e:
            print e
    
    
    def bind(self):
        try:
            self.s.bind((self.host, self.port))
        except Exception as e:
            print e
            
            
    def start_listening(self, numoflis):
        try:
            self.s.listen(numoflis)
        except Exception as e:
            print e
     
        
    def auto_init(self, num):
        try:
            self.start()
            self.bind()
            self.start_listening(num)
        except Exception as e:
            print e


    def close(self):
        try:
            self.s.close()
        except Exception as e:
            print e
            
            
    def tick(self):
        print ""
        
        
        
class Util():
    def __init__(self):
        print ""
        
    
    def redirect(self):
        print ""