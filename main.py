#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

DEFAULT_PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\n\tPath: %s\n\tHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST request\n\tPath: %s\n\tBody: %s\n",
                str(self.path), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Handler, port=DEFAULT_PORT):
    logging.basicConfig(filename='log',
                                filemode='a',
                                format='[%(asctime)s.%(msecs)d]\n%(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Server startup\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Server shutdown\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        print('serving on port %d' % DEFAULT_PORT)
        run()
