from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleMicroservice (BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response (200)
    self.send_header("Content-type", "text/plain")
    self.end_headers()
    self.wfile.write(b"Hello from microservice")
  
if_name='main_':
  server_address = ('',5000)
  httpd = HTTPServer (server_address, SimpleMicroservice)
  print("server running on port 5000...")
  httpd.serve_forever()
