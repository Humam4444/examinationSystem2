from flask import Flask
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import the Flask app from the parent directory
from app import app as flask_app

def handler(event, context):
    """Netlify function handler to process requests through Flask app."""
    path = event.get('path', '').lstrip('/')
    http_method = event['httpMethod']
    
    headers = event.get('headers', {})
    query_string = event.get('queryStringParameters', {}) or {}
    body = event.get('body', '')
    
    # Convert Netlify's event format to WSGI format
    environ = {
        'REQUEST_METHOD': http_method,
        'PATH_INFO': f'/{path}',
        'QUERY_STRING': '&'.join([f'{k}={v}' for k, v in query_string.items()]),
        'CONTENT_LENGTH': str(len(body) if body else 0),
        'wsgi.input': body,
        'HTTP_HOST': headers.get('host', 'localhost'),
    }
    
    # Add all headers
    for key, value in headers.items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            key = f'HTTP_{key}'
        environ[key] = value
    
    # Flask response
    response_status = [200]
    response_headers = []
    response_body = []
    
    def start_response(status, headers):
        response_status[0] = int(status.split(' ')[0])
        response_headers[:] = headers
    
    # Get response from Flask app
    response = b''.join(flask_app.wsgi_app(environ, start_response))
    
    # Convert headers to Netlify format
    headers_dict = {key: value for key, value in response_headers}
    
    # Return response in Netlify function format
    return {
        'statusCode': response_status[0],
        'headers': headers_dict,
        'body': response.decode('utf-8'),
        'isBase64Encoded': False
    }
