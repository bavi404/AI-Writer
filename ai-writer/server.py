from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

# Create outputs.txt if it doesn't exist
if not os.path.exists('outputs.txt'):
    open('outputs.txt', 'w').close()

# Start the server
port = 8080
print(f"Starting server on port {port}...")
print(f"Open http://localhost:{port} in your browser")
print("Make sure Ollama is running and the Mistral model is installed")
print("Press Ctrl+C to stop the server")

HTTPServer(('localhost', port), CORSRequestHandler).serve_forever() 