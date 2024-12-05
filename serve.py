
# Import necessary modules
import http.server
import socketserver

# Define the port and directory
PORT = 5000
DIRECTORY = "D:\数字人文工坊\合成游戏\daxigua-1.0.0\daxigua\index.html"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    # Set the directory for serving files
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Start the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Serving files from: {DIRECTORY}")
    httpd.serve_forever()