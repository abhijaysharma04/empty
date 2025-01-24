import json
from http.server import BaseHTTPRequestHandler
import os
from urllib.parse import parse_qs
from http import HTTPStatus

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.end_headers()

        # Log the path for debugging
        print(f"Path: {self.path}")

        # Parse query parameters
        query = parse_qs(self.path[2:])
        print(f"Query Parameters: {query}")
        names = query.get('name', [])

        # Marks data (simulated)
        marks_data = {
            'X': 10,
            'Y': 20,
            'Z': 30  # Example students and marks
        }

        # Collect the marks for the requested names
        marks = [marks_data.get(name, 0) for name in names]

        # Return the JSON response
        response = {'marks': marks}
        print(f"Response: {response}")  # Debugging response
        self.wfile.write(json.dumps(response).encode('utf-8'))
