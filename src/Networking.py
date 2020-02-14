# Writen by OneOneNot
# 14/2/2020
# No liesence

import socket
import Util

# This class handles client data
class Client():
    
    def __init__(self, uuid):
        self.ip = "0.0.0.0"
        self.port = 0000
        self.cookie = ""
        self.uuid = uuid
        
    # This function saves the user data in a file   
    def save_client(self, logfile):
        sep = "\n"
        client = self.uuid + self.ip + self.cookie
        f = open(logfile, "r")
        prlog = f.read()
        f.close()
        f = open(logfile, "w")
        f.write(prlog + sep + client)
        
    # This function loads a user from the log using the uuid    
    def load_client_by_uuid(self, logfile, uuid, mode):
        found = False
        f = open(logfile, "r")
        string = f.readline()
        fuuid = Util.get_log_uuid(string)
        while not found:
            if fuuid is uuid:
                found = True
                if mode is 1:
                    self.uuid = uuid
                    self.ip = Util.get_log_ip(string)
                    self.cookie = Util.get_log_cookie(string)
                break
                return 1
            else:
                string = f.readline()
                fuuid = Util.get_log_uuid(string)
        
        
    # This function loads a user from the log using the cookie   
    def load_client_by_cookie(self, logfile, cookie, mode):
        found = False
        f = open(logfile, "r")
        string = f.readline()
        fcookie = Util.get_log_cookie(string)
        while not found:
            if fcookie is cookie:
                found = True
                if mode is 1:
                    self.uuid = Util.get_log_uuid(string)
                    self.ip = Util.get_log_ip(string)
                    self.cookie = Util.get_log_cookie(string)
                break
                return 1
            else:
                string = f.readline()
                fcookie = Util.get_log_cookie(string)
    
    
    def get_user_data(self):
        print ""
        
        
    def delete_user(self):
        print ""
        
        
    def delete_global_user(self):
        print ""
        
        
    def new_user(self, ip):
        print ""
        
        
    def update_client(self, logfile):
        self.save_client(logfile)


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
        
        
        
