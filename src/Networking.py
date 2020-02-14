# Writen by OneOneNot
# 14/2/2020

import socket


class Client():
    # This class handles client data
    def __init__(self, uuid):
        self.ip = "0.0.0.0"
        self.port = 0000
        self.cookie = ""
        self.uuid = uuid
        
        
    def save_client(self, logfile):
        sep = "\n"
        client = self.ip + self.cookie
        f = open(logfile, "r")
        prlog = f.read()
        f.close()
        f = open(logfile, "w")
        f.write(prlog + sep + client)
        
        
    def load_client(self, logfile):
        print ""
        
    
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