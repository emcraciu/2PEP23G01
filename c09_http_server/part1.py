import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler

with open('index.html', 'r') as file:
    html = file.read()
    # soup = BeautifulSoup(file, 'html.parser')
    # object = soup.find('table')
    # object.new_tag('tr')
    # print(object)


class WebPhoneBook(BaseHTTPRequestHandler):
    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer):
        self.html = html
        super(WebPhoneBook, self).__init__(request, client_address, server)

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # app1: add 3 users with phone number
        self.html = self.html.format("""
    <tr>
        <td align="left">Ana</td>
        <td align="left">007564343</td>
    </tr>
""" + """\n{}""")
        print(self.html)
        self.wfile.write(self.html.encode())
#
#     def do_POST(self):
#         # print('done')
#         # print(self.headers['test'])
#         # print(self.headers['content-type'])
#         print(self.rfile.read(1))
#         # print(self.headers['Name'])
#         # print(self.headers['Number'])
#         self.html = self.html.format(f"""
#     <tr>
#         <td align="left">{self.headers['Name']}</td>
#         <td align="left">{self.headers['Number']}</td>
#     </tr>
# """ + """\n{}""")
#         print(self.html)
#         self.send_response(200)


http_server = HTTPServer(('localhost', 8082), WebPhoneBook)
http_server.serve_forever()
