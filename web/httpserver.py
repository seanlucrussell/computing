import http.server
import socketserver
import sqlite3

from io import BytesIO

PORT = 8080

'''
next steps:
add finished task list
update database with POST requests (for now ignore priority. 1st: completing
tasks)
'''

def get_data():
    conn = sqlite3.connect('/Users/seanrussell/Documents/Computing/web/database.db')
    c = conn.cursor()
    data = ""
    for row in c.execute('SELECT * FROM tasks'):
        parsed_row = str(row).replace('(','').replace(')','').split(',')
        status = ' checked' if parsed_row[2][1] == '1' else ''
        data += '<p>' + parsed_row[1][2:-1] + ' - <input type="checkbox"' + status + '></p>'
    conn.close()
    return data.encode()

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        self.wfile.write(get_data())

    def do_POST(self):
        '''DON'T DUPLICATE TASKS'''
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = body.decode('utf-8')
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'Adding new task')
        print('Adding new task:', body)
        conn = sqlite3.connect('/Users/seanrussell/Documents/Computing/web/database.db')
        c = conn.cursor()
        c.execute('INSERT INTO tasks VALUES (1, "' + body + '", FALSE)')
        conn.commit()
        conn.close()
        
        self.wfile.write(response.getvalue())

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
