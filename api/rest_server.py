#!/usr/bin/env python3

#########################
#
# Server-side script for RESTful API sever written in python using json
#
# The directory structure essentially defines the API. Each directory requires the following files:
#   verb = get, put, post, delete
#   <verb>.py performs the actions of the verb. For a get, it builds a JSON Data structure returned
#   <verb>.txt describes the API
#   <verb>.json defines the JSON schema
#
# Both client-side and server-side scripts are required for the API to work
#
# The default path to the API directory is /home/pi/api
#
#########################


#########################
#
# To run the script:
#   $ python3 /home/pi/api/rest_server.py
# or to run without waiting
#   $ python3 /home/pi/api/rest_server.py &
#
# There are multiple ways for a client-side to communicate with the Server-side API (see Help)
#
# This script requires the following:
#   Two raspberry pis: one running the server-side script (rest_server.py) and the other running 
#   the client-side script (rest_client.py)
#
#   Add the requests and distro modules:
#      $ pip install requests
#      $ sudo pip3 install distro
#
# Improvements
#   ??? how does importing this as a module work? or will it work
#   ??? renewing the cert should be part of the API, as long as the request is secure
#       certs should have their own directory within api
#   ??? add post, put and delete - but this can wait for actual usage example
#
# Each resource has one or more python script verbs (get.py, put.py)
# Sample directory Structure:
#    api
#       get.py
#       get.json
#       get.txt
#       server
#          get.py
#          get.json
#          get.txt
#          os
#             get.py
#             get.json
#             get.txt
#          memory
#             get.py
#             get.json
#             get.txt
#
# HTTP status codes:
#   1xx informational - not used
#   2xx success
#       200 OK for Get
#       201 Resource created for Post
#   3xx redirection - not used
#   4xx client error
#       400 Bad Request
#       401 Unauthorized: server not on LAN or bad HTTPS cert
#       404 Not Found
#   5xx web server error
#
# My understanding of Hypermedia as the Engine of Application State(HATEAOS),
# which guided implementation:
#   Client-Sever model: the rest and client scripts
#   Stateless: the web server is stateless.
#      If necessary, the client maintains state
#   Cacheable: resources are identified by the webserver as cacheable by the client
#   Uniform interface
#      Resource-Based: resources are identified in requests using URIs
#      Modification: resources are manipulated through API verbs (POST, PUT, GET, DELETE)
#      Self-descriptive client messages: a message contains sufficient information to describe
#         how a client can process a message
#         For example, a resource that allows POST, must support GET, which returns schema
#      Client can use API with no a priori knowledge, except base URI of API (i.e., discoverable)
#         So, versioning is not required
#         The entry URI provides a navigation resource (i.e., an object of all other URIs)
#            Navaigation includes allowed verbs (get, post, put, delete) on the URI and
#            whether or not the resource is cacheable (i.e., values in object are constant)
#         Other URIs: return the resource, which includes
#            resource object, its schema (how to the client can interpret the object) and/or
#            a status code
#   Layered system: client cannot tell if it is connected to end system or intermediary
#   Code on demand (optional)
#      For my applications, an SQL query can be passed to the web server
#   Idempotency: same object returned for the same call (values within object may change)
#      POST is NOT idempotent.
#      GET, PUT and DELETE are idempotent (e.g., delete should return same return code if
#      resource does not exist)
#
# HTTP Verbs:
#   GET: Provides read-only access to a resource
#   POST: Create a resource
#   DELETE: Delete a resource
#   PUT: Modify an existing resource (POST is use for creating a resource)
#
# Multithreading
#   I doubt my home systems will be transferring large files or have such a large volume of
#   API requests that multithreading would be required. In the course of putting together this
#   script, I ran across several instances of multithreaded http and https servers. Perhaps,
#   multithreading is a requirement and I am not in a position to see it yet. So, I'll add it.
#   g10guang's post 27JUL2018 in stackoverflow seems to be the most straight forward.
#
# HTTP and HTTPS support
#   In general, only servers that are authorized to use the API should be allowed, which
#   requires opening an SSL socket using a cert.
#
#   Run these commands on the server (use defaults and for FQDN use hostanme.local):
#
#      $ openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
#      $ openssl req -x509 -newkey rsa:4096 -nodes -out client.crt -keyout client.key -days 365
#
#   copy the server.crt, client.key and client.crt to the rest_client server
#
#########################


#########################
# import needed libraries
import time
import datetime
import distro
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import socket
import re
import os
import subprocess
import sys
import getopt
import ipaddress
import ssl
import json
import socket
import psutil


#########################
# use all CAPs for constants
MY_LAN = '192.168.1.0/24'


#########################
# use first CAP for global variables
#
# use high numbered port (e.g., 90xx) indicating it is using http (port 80) and 9443 for https
Port = 9080
InputFile = ''
OutputFile = ''
Path = '/home/pi/api'
LogFile = Path + '/rest_server.log'
Use_HTTPS = False
Use_cert = False
Use_multithreading = False
ServerKeyFile = Path + '/server.key'
ServerCertFile = Path + '/server.crt'
ClientCertFile = Path + '/client.crt'
Debug = False

#########################
# Log messages should be time stamped
def timeStamp():
    t = time.time()
    s = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S - ')
    return s

def printMsg(s):
    if s == '':
        LogFileObject.write("\n")
        if Debug:
            print('')
    else:
        LogFileObject.write(timeStamp() + s + "\n")
        if Debug:
            print(timeStamp() + s)

    LogFileObject.flush()


#########################

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class customHandler(BaseHTTPRequestHandler):
    def getClient(self):
        c = str(self.client_address[0]) + " " + str(self.client_address[1])
        printMsg('Client is: ' + c)
        return(c)

    # only allow the API to be used by other servers on my LAN
    def isClientIpInvalid(self):
        network= ipaddress.ip_network(MY_LAN)
        client = ipaddress.ip_address(self.client_address[0])
        if (client in ipaddress.ip_network(MY_LAN)):
            printMsg('Client IP is valid: ' + str(client))
            return(False)
        printMsg('Client IP is invalid')
        self.sendInvalid('Client IP address is invalid')
        return(True)

    def sendIcon(self):
        # returns icon for the webserver
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        with open(Path + "/favicon.png", "rb") as fout:
            self.wfile.write(fout.read())
        return

    def sendHeaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        return

    def sendInvalid(self, s):
        printMsg(s + '\n')
        self.send_error(404, message=s)
        self.send_header('Content-type','text/html')
        self.end_headers()
        return

    def do_GET(self):
        # GET provides read-only access to the server's resources
        global Data

        pc = Path.split("/")
        l = len(pc) - 1
        no_api_path = ""
        for i in range(l):
            if pc[i] != "":
                no_api_path += "/" + pc[i]

        printMsg(self.requestline)
        printMsg(self.getClient())
        if Use_multithreading:
            printMsg('Thread: ' + str(threading.currentThread().getName()) + ' ' + str(threading.active_count()))

        if self.isClientIpInvalid():
            return

        if None != re.search('/api', self.path):
            data = {}
            try:
                exec(open(no_api_path + self.path + "/" + "get.py").read())
                data = Data
                self.sendHeaders()
                self.wfile.write(bytes(json.dumps(data), 'utf-8'))
                printMsg('')
                return
            except:
                # unhandled resource
                self.sendInvalid('Invalid resource requested')
                printMsg('Invalid resource requested' + '\n')
                printMsg('')
                return
        elif None != re.search('/favicon.ico', self.path):
            # This is not part of the API, but browsers may request a favicon.ico to display in the tab
            self.sendIcon()
            printMsg('')
            return
        else:
            self.sendInvalid('Invalid request')
            printMsg('Invalid request' + '\n')
            printMsg('')
            return

    def do_POST(self):
        # POST allows client to add a new resource on the server
        # ??? needs work should follow get
        # successful request returns a 201
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("POST Request", "utf8")
        printMsg('')
        return

    def do_DELETE(self):
        # DELETE allows a client to remove a server's resources
        # ??? needs work should follow get
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("DELETE Request")
        printMsg('')
        return

    def do_PUT(self):
        # PUT alllows client to update an existing resource
        # ??? needs work should follow get
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("PUT Request")
        printMsg('')
        return

    def handle_http(self):
        return

    def respond(self):
        return

def cmdLine(argv):
    global InputFile
    global OutputFile
    global Port
    global LogFile
    global Use_HTTPS
    global Use_cert
    global Debug
    global Use_multithreading

    port_set = False
    try:
        # new options must be added here:
        validOpts = "hcdi:l:mp:s"
        opts, args = getopt.getopt(argv,validOpts,["help=", "cert", "debug", "inputfile=", "logfile=", "multithreading", "port=", "secure"])
    except getopt.GetoptError:
        print('rest_server.py [options, ...]' )
        print('rest_server.py -h' )
        sys.exit(2)

    for opt, arg in opts:
        # help option goes first and exits, regardless of other options
        if opt in ('-h', "--help"):
            print('Decription: ')
            print('  Server-side script for RESTful API sever written in python using json')
            print('  Replace angle brackets with actual value.')
            print('  There are multiple ways for a client-side server to communicate with this server-side API:')
            print('    A client-side script can make HTTP requests (see rest_client.py)')
            print('    Open a browser and enter: http://<server-hostname>:<port>/api/cpu')
            print('    Open a terminal and run: $ curl -X GET http://<server-hostname>:<port>/api/cpu')
            print('')
            print('Usage:')
            print('  python3 rest_server.py [options...]')
            print('')
            print('Options:')
            print('  -h --help           this help')
            print('  -c --cert           Use cert, requires use https')
            print('  -d --debug          debug mode')
            print('  -i --inputfile      input json file')
            print('  -l --logfile        write log messages to user specified file')
            print('  -m --multithreading use multithreading')
            print('  -p --port           User defined port. The default port is' + str(Port) + '.')
            print('  -s --secure         use https')
            sys.exit()
        elif opt in ("-c", "--cert"):
            Use_cert = True
        elif opt in ("-d", "--debug"):
            Debug = True
        elif opt in ("-i", "--inputfile"):
            InputFile = arg
        elif opt in ("-l", "--logfile"):
            LogFile = arg
        elif opt in ("-m", "--multithreading"):
            Use_multithreading = True
        elif opt in ("-p", "--port"):
            Port = int(arg)
            port_set = True
        elif opt in ("-s", "--secure"):
            Use_HTTPS = True
            if port_set:
                pass
            else:
                Port = 9443
    return

def printCmdLine():
    printMsg('Command line arguments:')
    printMsg('  Input file  = ' + InputFile)
    printMsg('  Log file = ' + LogFile)
    printMsg('  Port = ' + str(Port))
    printMsg('  Use cert = ' + str(Use_cert))
    printMsg('  Use HTTPS = ' + str(Use_HTTPS))
    printMsg('  Use multithreading = ' + str(Use_multithreading))
    printMsg('')
    return

#########################
def main(sysargv):
    global LogFileObject
    global Port

    # process command line arguments
    cmdLine(sysargv[1:])

    # open a log file. printMsg writes to the log file
    LogFileObject = open(LogFile, 'w+')

    printMsg("Starting REST server")
    printCmdLine()

    # get info about server-side host
    hostname = socket.gethostname()
    printMsg('Web Server:')
    printMsg("  Server name = " + hostname)
    local_host_ip = socket.gethostbyname(hostname)
    printMsg("  Server IP = " + local_host_ip)
    printMsg('')

    host_ip = subprocess.check_output(['hostname', '-s', '-I']).decode('utf-8')[:-1]
    printMsg("  Server IP = " + host_ip)
    printMsg('')

    # create a handle for the server-side using the host information
    rest_server = (local_host_ip, Port)

    if Use_multithreading:
        # threaded server
        httpd = ThreadingSimpleServer(rest_server, customHandler)
    else:
        # non-threaded server
        httpd = HTTPServer(rest_server, customHandler)

    if Use_HTTPS and Use_cert:
        printMsg("  Using HTTPS and cert")
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain(certfile=ServerCertFile, keyfile=ServerKeyFile)
        context.load_verify_locations(cafile=ClientCertFile)

    # The server will run forever unless interrupted by CTRL-c
    try:
        if Use_HTTPS:
             if Use_cert:
                 httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
                 printMsg("  Got socket for HTTPS and cert")
             else:
                 httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=ServerKeyFile, certfile=ServerCertFile$
                 printMsg("  Got socket for HTTPS with no cert")
        else:
             printMsg("  No socket is required for HTTP?")

        httpd.serve_forever()
                                                
    except KeyboardInterrupt:
        pass

    # close server and files
    httpd.server_close()
    printMsg("Closing REST server")
    exit()

#########################
if __name__ == '__main__':
    # run as a script from command line
    main(sys.argv)
else:
    # ??? could allow import to another module; needs some work
    pass
