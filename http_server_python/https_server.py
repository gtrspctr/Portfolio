#!/usr/bin/env python

"""
This is an http server.

Its GET request handler will serve various web pages.

Unfortunately, I ran out of time before I could get the
POST request handler working.

I took ideas and lessons from lots of places, but did
very few direct copies. There is a "credits" file in 
the current directory with my sources.
At the code that was copied or heavily influnced by, I will
put a comment with a number that corresponds to a URL in the
"credits" file.

This application was written by Al Robison.
Last Modified:  2023/01/26
"""

from http.server import HTTPServer, BaseHTTPRequestHandler 
import ssl
from os import path
import json
import cgi   # Not currently used. Possible use for POST requests.

# Define the host IP and port number
# An IP of 0.0.0.0 will broadcast on all local NICs
# 443 is the standard port for HTTPS
host_addr = "0.0.0.0"
port = 443

# Define the local filepaths of the Public
# and Private keys.
# Source 10
cert_file = path.abspath("/etc/letsencrypt/live/alrobison.com/fullchain.pem")
key_file = path.abspath("/etc/letsencrypt/live/alrobison.com/privkey.pem")

# Request handler class
# Source 1
# Source 2
# Source 3
# Source 4
class AlsRequestHandler(BaseHTTPRequestHandler):
	# do_GET sends a response of 200 when
	# successful. It also specifies content type
	# of headers, and will display or "send" data
	# back to the client.
	def do_GET(self):
		self.send_response(200)

		# self.path is the end of the URL (after ".com")
		# Based on the path, you can send different content.
		if self.path == "/":
			# Home page
			self.path = "/index.html"
			self.send_header("Content-type", "text/html")
			self.end_headers()

			# Website body
			# This sends the contents of an HTML file to the
			# requestor, in the form of bytes and encoded
			# in utf-8.
			self.wfile.write(bytes(index_output, "utf-8"))

		elif self.path == "/users":
			# Web page containing a JSON structure.
			# The Content-Type indicates to the browser that
			# the data is supposed to be formatted as JSON.
			self.send_header("Content-type", "application/json")
			self.end_headers()

			self.wfile.write(bytes(json_output, "utf-8"))
		elif self.path == "/files":
			# Web page that displays a place to upload files
			self.send_header("Content-type", "text/html")
			self.end_headers()

			self.wfile.write(bytes(files_output, "utf-8"))
		else:
			# Any other URL suffix.
			# For example, https://alrobison.com/contact
			# would lead to this page.
			self.send_header("Content-type", "text/html")
			self.end_headers()

			self.wfile.write(bytes(unkn_output, "utf-8"))

	def do_POST(self):
		# do_POST() handles all POST requests.
		# I ran out of time before I could figure out how to
		# successfully receive (or POST) data.
		# So this doesn't really do much besides send a
		# response and a message in utf-8 bytes.
		self.send_response(201)
		if self.path == "/upload":
			# If working, this would be the URL that is called
			# when a file is uploaded.
			self.wfile.write(bytes("POST request received!", "utf-8"))

			# Below are some remnants of non-working code.
			# These are various ideas and rabbit holes I went
			# down in my quest to figure this out.
			# Leaving these here just to show that I tried :)
			"""
			target_path = file_repo
			filename = path.basename(self.path)
			self.wfile.write(bytes("Target:" + target_path, "utf-8"))
			self.wfile.write(bytes("Filename:" + filename, "utf-8"))
			"""

			"""file_length = int(self.headers["Content-Length"])
			with open(filename, "wb") as output_file:
				output_file.write(self.rfile.read(file_length))
			self.end_headers()
			reply_body = "Saved '%s'\n" % filename
			self.wfile.write(bytes(reply_body, "utf-8"))"""

			"""
			ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
			print("CTYPE: " + str(ctype))
			print("PDICT: " + str(pdict))
			if ctype == 'multipart/form-data':
				cgi.parse_multipart(self.rfile, pdict)
			elif ctype == 'application/x-www-form-urlencoded':
				lenth = int(self.headers['content-length'])
				parse_qs(self.rfile.read(length), keep_blank_values=1)
			"""

			"""
			ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
			if ctype == "multipart/form-data":
				fields = cgi.parse_multipart(self.rfile, pdict)
			"""
			"""
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(bytes(str(json_obj), "utf-8"))
			"""

	# Below are functions that are supposed to run
	# the different actions specified in Max's
	# instructions. Right now they don't do anything
	# except requestAllContent().
	def requestValue(self):
		pass

	def requestAllContent(self):
		return json_obj

	def updateValue(self):
		pass

	def deleteDict(self):
		pass

	def deleteDictStructure(self):
		pass

# readFiles() takes a 'source' file and
# an 'output' location (a str variable).
# It opens and reads the contents of the
# 'source' file and stores it in the 'output'.
# The point is to verify the html/json
# content files are present. If not, print
# a message and exit.
def readFiles(source, output):
	try:
		with open(source, "r") as reader:
			output = reader.read()
		return output
	except FileNotFoundError as fnfe:
		print("HTML source file is not present")
		exit(1)
	except:
		print("Something went wrong.")
		exit(1)

# Define local filepaths
server_path = path.dirname(__file__)		# Current working directory
content_repo = path.join(server_path,		# Web page data directory
						 "content_repository")
index_source = path.join(content_repo,		# Index HTML content
						 "index.html")
unknown_source = path.join(content_repo,	# Unknown page HTML content
						   "unknown.html")
files_source = path.join(content_repo,		# File upload HTML content
						  "files.html")
json_source = path.join(content_repo,		# JSON content
						"users.json")
file_repo = path.join(server_path,			# Repository for file uploads
					  "file_repository")

# Define output files and store HTML/JSON content
index_output = ""
json_output = ""
unkn_output = ""
files_output = ""
index_output = readFiles(index_source, index_output)
json_output = readFiles(json_source, json_output)
unkn_output = readFiles(unknown_source, unkn_output)
files_output = readFiles(files_source, files_output)

# Get JSON data as an object
# Was to be used in POST requests.
json_obj = json.loads(json_output)

# Create HTTPServer object, passing in the addr/port
# and request handler object.
server = HTTPServer((host_addr, port), AlsRequestHandler)

# Create SSL Context.
# This basically wraps the HTTPServer object to secure
# its communication with a client.
# Source: 7
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.check_hostname = False
ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)
server.socket = ssl_context.wrap_socket(server.socket,
										server_side=True)

try:
	server.serve_forever()  # Start the HTTPServer
except KeyboardInterrupt:	# Control + C
	server.server_close()   # Exit the

print()
print("Server connection terminated.")
