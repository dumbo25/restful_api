#!/usr/bin/env python3

#########################
#
# Server-side script for RESTful API sever written in python using json
#
# Both client-side and server-side scripts are required for the API to work
#
#########################


#########################
#
# The script runs with this command:
#   $ python3 rest_server.py
#
# There are multiple ways for a client-side to communicate with this Server-side API (see Help)
#
# This script requires the following:
#   Two raspberry pis: one running the server-side script and the other running the client-side script
#
#   Add the requests and distro modules:
#      $ pip install requests
#      $ sudo pip3 install distro
#
#   Install sqlite3 and inxi:
#      $ sudo apt-get install sqlite3 -y
#      $ sudo apt-get install inxi -y
#
#   Create databse and a table and then exit sqlite
#      $ sqlite3 api.db
#      sqlite > BEGIN;
#      sqlite > CREATE TABLE status (tdate DATE, ttime TIME, uri TEXT, verbs TEXT, cacheable TEXT);
#      sqlite > COMMIT;
#      sqlite> .quit
#
#   Move the database and change the permissions
#      $ sudo mv security.db /var/www/db/api.db
#      $ sudo chmod og+rw /var/www/db
#      $ sudo chmod og+rw /var/www/db/api.db
#
# Improvements
#   ??? /api needs a get.py
#   ??? each relative directory needs a json file associated with get (and other verbs ???)
#      ??? need to read and write json for /rel in /api navigation
#   ??? Client must keep state information
#   ??? Versioning is not used in HATEOAS - must remove
#   ??? client-side needs to be enhanced to get navigation from web server
#   ??? client-side can cache
#   ??? client should be able to understand and navigate API by starting at root URI
#   ??? need example of: Get, Post, Delete and Put
#   ??? update scripts on github
#
# Each resource has one or more python script verbs (get.py, put.py)
# Sample directory Structure:
#   path
#      api
#         get.py
#         get.json
#         hostname.db
#         server
#            get.py
#            get.json
#            os
#               get.py
#               get.json
#            memory
#               get.py
#               get.json
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
#         This means versioning is not required
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
#   In general, only servers that are authorized to use the API should be allowed to do so. This
#   requires opening an SSL socket using a cert.
#
#   Run these commands on the server (use defaults and for FQDN use hostanme.local):
#
#      $ openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
#      $ openssl req -x509 -newkey rsa:4096 -nodes -out client.crt -keyout client.key -days 365
#
#   copy the server.crt, client.key and client.crt to the rest_client server
#
#   ??? renewing the cert should be part of the API, as long as the request is secure
#
# Versioning ??? need to remove this
#   At a minimum, rest_server.py needs to handle current version, last version and next version.
#   It could handle many more old versions. The client should provide the version it needs.
#   As an example, say the current version is 1.1, then rest_server.py should support 1.0 (last)
#   and 2.0 or 1.2 next version. The version is passed through a json file or header
#   For, rest_client.py Content-Type header should include:
#
#      version:1.0
#      version:1.1
#      version:2.0
#
#   and then the rest_server.py has an Accept *
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
# use high numbered port (90xx) indicating it is using http (port 80) and 9443 for https
Port = 9080
InputFile = ''
OutputFile = ''
Path = '/home/pi/'
LogFile = Path + 'rest_server.log'
Use_HTTPS = False
Use_cert = False
Use_multithreading = False
ServerKeyFile = Path + 'server.key'
ServerCertFile = Path + 'server.crt'
ClientCertFile = Path + 'client.crt'

#########################
# Log messages should be time stamped
def timeStamp():
    t = time.time()
    s = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S - ')
    return s

# Write messages in a standard format
def printMsg(s):
    if s == '':
        LogFileObject.write("\n")
    else:
        LogFileObject.write(timeStamp() + s + "\n")

    LogFileObject.flush()

#########################

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class customHandler(BaseHTTPRequestHandler):
    def getClient(self):
        c = str(self.client_address[0]) + " " + str(self.client_address[1])
        return(c)

    # only allow the API to be used by other servers on my LAN
    def isClientIpInvalid(self):
        network= ipaddress.ip_network(MY_LAN)
        client = ipaddress.ip_address(self.client_address[0])
        if (client in ipaddress.ip_network(MY_LAN)):
            return(False)
        self.sendInvalid('Client IP address is invalid')
        return(True)

    def sendIcon(self):
        # returns icon for the webserver
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        with open("favicon.png", "rb") as fout:
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

    def readVersion(self):
        global Version

        if self.headers != '':
            Version = self.headers['version']
        return

    def addSpaces (self, n):
        s = ""
        if n > 0:
            for i in range(n):
                s += "    "
        return(s)

    def getSchema(self, file):
        try:
            # ??? how to get proper indentation
            schema = "\"schema\" : { \n"
            with open(file + ".json", "r") as read_file:
                schema += read_file.read()
            schema += "},\n"
        except:
            schema = "\"schema\" : { },\n"
        return(schema)

    def getNavigation(self):
        # returns navigation for API
        # ??? build navigation with resource json goes here
        # ??? move this function to /api/get.py

        root = Path[:len(Path)-1]
        next = False
        last_level = 0

        bracket = 0     # bracket = [
        brace = 0       # brace   = {

        data = "{\n"
        brace += 1

        for paths, dirs, files in os.walk(Path + 'api'):
            schema = "\"schema\" : { },\n"
            verbs = "\"verbs\" : ["
            next_verb = False
            for f in files:
                if None != re.search('.py', f):
                    if next_verb:
                        verbs += ", "
                    verb = f[:len(f)-3]
                    schema = self.getSchema(paths + "/" + verb)
                    verb = verb.upper()
                    verbs += "\"" + verb + "\""
                    next_verb = True
            verbs += "],\n"

            p = paths[len(root):]
            # /api splits into a null entry and api
            # so the len is one more than expected
            pc = p.split("/")
            level = len(pc) - 1

            if (level == last_level):
                # same level as before
                if (last_level == 0):
                    # level should never be 0
                    print("XX ****** Error ****** \n")
                else:
                    # same last_level
                    brace -= 1
                    s = self.addSpaces(brace+bracket)
                    data += s + "AA}\n"

                    bracket -= 1
                    s = self.addSpaces(brace+bracket)
                    data += s + "]\n"

                    brace -= 1
                    s = self.addSpaces(brace+bracket)
                    data += s + "}, {\n"
                    brace += 1

                    s = self.addSpaces(brace+bracket)
                    data += s + "\"rel\" : \"" + pc[level] + "\",\n"
                    data += s + verbs
                    data += s + "\"description\" : \"returns server date and time\",\n"
                    data += s + schema
                    data += s + "\"links\": [\n"
                    bracket += 1

                    s = self.addSpaces(brace+bracket)
                    data += s + "{\n"
                    brace += 1

                    level = last_level + 1
            elif (level == (last_level+1)):
                # increasing by one level
                if (last_level == 0):
                    # at first level
                    s = self.addSpaces(brace+bracket)
                    data += s + "BB\"rel\" : \"" + pc[level] + "\",\n"
                    data += s + verbs
                    data += s + "\"description\" : \"returns server date and time\",\n"
                    data += s + schema
                    data += s + "\"links\": [\n"
                    bracket += 1

                    s = self.addSpaces(brace+bracket)
                    data += s + "{\n"
                    brace += 1

                    last_level = last_level + 1
                else:
                    # increasing a level and not at beginning
                    s = self.addSpaces(brace+bracket)
                    data += s + "CC\"rel\" : \"" + pc[level] + "\",\n"
                    data += s + verbs
                    data += s + "\"description\" : \"returns server date and time\",\n"
                    data += s + schema
                    data += s + "\"links\": [\n"
                    bracket += 1

                    s = self.addSpaces(brace+bracket)
                    data += s + "{\n"
                    brace += 1

                    last_level = last_level + 1
            elif (level == (last_level-1)):
                # backing up a level
                if (last_level == 0):
                    # this should be the end
                    data +=" **** ERROR *****"
                else:
                    # backing up a level, but not at beginning
                    brace -= 1
                    s = self.addSpaces(brace+bracket)
                    data += s + "DD}\n"

                    bracket -= 1
                    s = self.addSpaces(brace+bracket)
                    data += s + "]\n"

                    if bracket >= 2:
                        brace -= 1
                        s = self.addSpaces(brace+bracket)
                        data += s + "}\n"

                        bracket -= 1
                        s = self.addSpaces(brace+bracket)
                        data += s + "]\n"

                    brace -= 1
                    s = self.addSpaces(brace+bracket)
                    data += s + "}, {\n"
                    brace += 1

                    s = self.addSpaces(brace+bracket)
                    data += s + "\"rel\" : \"" + pc[level] + "\",\n"
                    data += s + verbs
                    data += s + "\"description\" : \"returns server date and time\",\n"
                    data += s + schema
                    data += s + "\"links\": [\n"
                    bracket += 1

                    s = self.addSpaces(brace+bracket)
                    data += s + "{\n"
                    brace += 1
            else:
                data += "**** ERROR ****"

            # for f in files:
            #     print (f)
            next = True

        while (brace+bracket) > 0:
            if brace > 0:
                brace -= 1
                s = self.addSpaces(brace+bracket)
                data += s + "EE}\n"

            if bracket > 0:
                bracket -= 1
                s = self.addSpaces(brace+bracket)
                data += s + "FF]\n"

        print(data)
        return(data)

    def do_GET(self):
        # GET provides read-only access to the server's resources
        global Data

        self.readVersion()
        printMsg(self.requestline)
        printMsg(self.getClient())
        if Use_multithreading:
            printMsg('Thread: ' + str(threading.currentThread().getName()) + ' ' + str(threading.active_count()))

        if self.isClientIpInvalid():
            return

        if '/api' == self.path:
            Data = self.getNavigation()
            data = Data
            self.sendHeaders()
            self.wfile.write(bytes(json.dumps(data), 'utf-8'))
            printMsg('')
            return
        elif None != re.search('/api/mydata', self.path):
            self.sendHeaders()
            with open("/home/pi/data.json", "r") as read_file:
                data = json.load(read_file)
            self.wfile.write(bytes(json.dumps(data), 'utf-8'))
            printMsg('')
            return
        elif None != re.search('/api/server', self.path):
            data = {}
            file = Path + 'rest_server.tmp'
            print(self.path)
            try:
                exec(open(Path + self.path + "/" + "get.py").read())
                data = Data
                self.sendHeaders()
                self.wfile.write(bytes(json.dumps(data), 'utf-8'))
                printMsg('')
                return
            except:
                # unhandled resource
                self.sendInvalid('Invalid resource requested')
                printMsg('Invalid resource requested' + '\n')
                return
        elif None != re.search('/favicon.ico', self.path):
            # ??? add /favicon.ioc to api json file
            # browsers may request a favicon.ico to display in the tab
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
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("DELETE Request")
        printMsg('')
        return

    def do_PUT(self):
        # PUT alllows client to update an existing resource
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
    global Use_multithreading

    port_set = False
    try:
        # new options must be added here:
        validOpts = "hci:l:mp:s"
        opts, args = getopt.getopt(argv,validOpts,["help=", "cert", "inputfile=", "logfile=", "multithreading", "port=", "secure"])
    except getopt.GetoptError:
        print('rest_server.py [options, ...]' )
        print('rest_server.py -h' )
        sys.exit(2)

    for opt, arg in opts:
        # help option goes first and exits, regardless of other options
        if opt in ('-h', "--help"):
            print('Decription: ')
            print('  Server-side script for RESTful API sever written in python using json')
            print('  There are multiple ways for a client-side server to communicate with this server-side API:')
            print('    A client-side script can make HTTP requests (see rest_client.py)')
            print('    Open a browser and enter: http://security:9080/api/multi/10/23')
            print('    Open a terminal and run: $ curl -X GET http://security:9080/api/multi/10/23')
            print('')
            print('Usage:')
            print('  python3 rest_server.py [options...]')
            print('')
            print('Options:')
            print('  -h --help           this help')
            print('  -c --cert           Use cert, requires use https')
            print('  -i --inputfile      input json file')
            print('  -l --logfile        write log messages to user specified file')
            print('  -m --multithreading use multithreading')
            print('  -p --port           User defined port. The default port is' + str(Port) + '.')
            print('  -s --secure         use https')
            sys.exit()
        elif opt in ("-c", "--cert"):
            Use_cert = True
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
    host_ip = socket.gethostbyname(hostname)
    printMsg("  Server IP = " + host_ip)
    printMsg('')

    # create a handle for the server-side using the host information
    rest_server = (host_ip, Port)

    if Use_multithreading:
        # threaded server
        httpd = ThreadingSimpleServer(rest_server, customHandler)
    else:
        # non-threaded server
        httpd = HTTPServer(rest_server, customHandler)

    if Use_HTTPS and Use_cert:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain(certfile=ServerCertFile, keyfile=ServerKeyFile)
        context.load_verify_locations(cafile=ClientCertFile)

    # The server will run forever unless interrupted by CTRL-c
    try:
        if Use_HTTPS:
             if Use_cert:
                 httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
             else:
                 httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=ServerKeyFile, certfile=ServerCertFile, server_side=True)

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
    # import to another module
    pass
