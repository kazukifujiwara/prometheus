import http.server
import random

from prometheus_client import start_http_server, Counter

REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_worlds_exception_total', 'Exceptions serving Hello World.')
SALES = Counter('hello_worlds_sales_euro_total', 'Euros made serving Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @EXCEPTIONS.count_exceptions()
    def do_GET(self):
        REQUESTS.inc()
        euros = random.random()
        SALES.inc(euros)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Hello World for {euros} euros.".encode())
        
if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('', 8001), MyHandler)
    server.serve_forever()
    