#University of St. Thomas, Advanced Web Applications, SEIS752 Fall 2009
#Lloyd Cledwyn
#Basic Http Server example
#Adapted from http://wiki.python.org/moin/BaseHttpServer
import time
import BaseHTTPServer
from os import curdir, sep

#Define some variables to be used in the execution of the program
HOST_NAME = '' # can be 'localhost' or if you change your hosts.txt file, what happens?? ;)
PORT_NUMBER = 80 #If you kill the server un-gracefully you may need to change this to an open socket.

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
#MyHandler class implements standard standard HTTP menthods
#currently HEAD and GET requests are handled.      
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        #Respond to a GET request.
        try:
			if self.path == "/":
				f = open(curdir + sep + "index.html") #self.path has /index.html
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()
                # Start sending content
				self.wfile.write(f.read())
				f.close()
				return
				
			if self.path.endswith((".html",".htm")):
				f = open(curdir + sep + self.path) #self.path has /index.html
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()
                # Start sending content
				self.wfile.write(f.read())
				f.close()
				return
                
			if self.path.endswith(".time"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()
                # Send current time
				self.wfile.write("Are the children all in bed because now its " + str(time.localtime()[3]) + " O'Clock!!") 
				return
                
			if self.path.endswith(".gif"):
				f=open(curdir + sep + self.path, 'rb')
				self.send_response(200)
				self.send_header("Content-type", "image/gif")
				self.end_headers()
                # Start sending content
				self.wfile.write(f.read())
				f.close()
				return
           
                
			if self.path.endswith(".jpg"):
				f=open(curdir + sep + self.path, 'rb')
				self.send_response(200)
				self.send_header("Content-type", "image/jpg")
				self.end_headers()
                # Start sending content
				self.wfile.write(f.read())
				f.close()
				return
				
        except IOError:
            self.send_error(404,'File not found: %self' % self.path)
            
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer  #Instantiate a server object
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler) #Tell the serever what hostname & port to run on, then what handler to handle the server requests.
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()  #Run the server.
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
