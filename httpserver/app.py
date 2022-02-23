import http.server
import random
import time
import unittest

from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram, REGISTRY

'''
3.2章まで
'''

# REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')
# EXCEPTIONS = Counter('hello_worlds_exception_total', 'Exceptions serving Hello World.')
# SALES = Counter('hello_worlds_sales_euro_total', 'Euros made serving Hello World.')

# class MyHandler(http.server.BaseHTTPRequestHandler):
#     @EXCEPTIONS.count_exceptions()
#     def do_GET(self):
#         REQUESTS.inc()
#         euros = random.random()
#         SALES.inc(euros)
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(f"Hello World for {euros} euros.".encode())
        
# if __name__ == "__main__":
#     start_http_server(8000)
#     server = http.server.HTTPServer(('', 8001), MyHandler)
#     server.serve_forever()
    
'''
3.3.1 prometheus_client.Gauge
'''

# # Gaugeのカウンタメトリクスの末尾には_totalをつけないのが慣習
# INPROGRESS = Gauge('hello_worlds_inprogress', 'Number of Hello Worlds in progress.')
# LAST = Gauge('hello_worlds_last_time_seconds', 'The last time a Hello World was served.')

# class MyHandler(http.server.BaseHTTPRequestHandler):
#     @INPROGRESS.track_inprogress()
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(f"Hello World".encode())
#         LAST.set(time.time())
        
# if __name__ == "__main__":
#     start_http_server(8000)
#     server = http.server.HTTPServer(('', 8001), MyHandler)
#     server.serve_forever()
    
'''
3.4 prometheus_client.Summary
3.5 prometheus_client.Histogram
'''

# # LATENCY = Summary('hello_world_latency_seconds', 'Time for a request Hello World.')
# LATENCY = Histogram('hello_world_latency_seconds',
#                     'Time for a request Hello World.',
#                     buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1])

# class MyHandler(http.server.BaseHTTPRequestHandler):
#     @LATENCY.time()
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(f"Hello World".encode())
        
# if __name__ == "__main__":
#     start_http_server(8000)
#     server = http.server.HTTPServer(('', 8001), MyHandler)
#     server.serve_forever()
    
'''
3.6 Instrumentation(測定) Test
'''

FOOS = Counter('foos_total', 'The number of foo calls.')

def foo():
    FOOS.inc()
    
class TestFoo(unittest.TestCase):
    def test_counter_inc(self):
        before = REGISTRY.get_sample_value('foos_total')
        foo()
        after = REGISTRY.get_sample_value('foos_total')
        self.assertEqual(1, after-before)

class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Hello World".encode())
        
if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('', 8001), MyHandler)
    server.serve_forever()