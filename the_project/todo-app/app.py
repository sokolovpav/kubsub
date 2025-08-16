from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        port = int(os.getenv('PORT', '8080'))  # Default to 8080 if PORT not set
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = f"Server is running on port {port}"
        self.wfile.write(message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleServer):
    port = int(os.getenv('PORT', '8080'))  # Default to 8080 if PORT not set
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started in port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()