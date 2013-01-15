import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])+" "+self.data
        self.request.sendall("You made a mistake: '" + self.data + "' is meant to say '#YOLOSWAG'")

HOST, PORT = "localhost", 597
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()