from http.server import BaseHTTPRequestHandler, HTTPServer
from LLM import LLM
import json

llm=LLM()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path.endswith('.css'):
            self._set_response(200, 'text/css')
            with open(self.path[1:], 'rb') as css_file:
                self.wfile.write(css_file.read())
            return
        elif self.path.endswith('.png'):  # Handle .png image requests
            self._set_response(200, 'image/png')
            with open(self.path[1:], 'rb') as image_file:
                self.wfile.write(image_file.read())
            return
        elif self.path.endswith('.pdf'):  # Handle .pdf image requests
            self._set_response(200, 'application/pdf')
            with open(self.path[1:], 'rb') as image_file:
                self.wfile.write(image_file.read())
            return
        try:
            file_to_open = open(self.path[1:],'r',encoding='utf-8').read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self._set_response()
        self.wfile.write(file_to_open.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        print(data)
        try:
            query    = data['query']
            answer   = llm.get_QA(query)
            print(answer)
            response = {'answer': answer}
            self._set_response(200, 'application/json')
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except:
            self._set_response(400, 'application/json')
            self.wfile.write(json.dumps({'error': 'Invalid input'}).encode('utf-8'))    

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()