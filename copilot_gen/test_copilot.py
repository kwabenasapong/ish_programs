#!/usr/bin/env python3
"""Test the copilot module with flask web server."""

import unittest
import logging
import logging.config

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_socketio import SocketIO

from copilot import Copilot

# Set up logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('copilot')

# Set up flask
app = Flask(__name__)

# Set up flask_restful
api = Api(app)

# Set up flask_cors
CORS(app)

# Set up flask_socketio
socketio = SocketIO(app, cors_allowed_origins="*")

# Set up flask_httpauth
auth = HTTPBasicAuth()

# Set up flask_jwt_extended

# Set up copilot
copilot = Copilot()

# Path: test_copilot.py
if __name__ == '__main__':
    # Set up flask
    app.run(debug=True, host='0.0.0.0', port=5000)


# Path: test_copilot.py
class TestCopilot(unittest.TestCase):
    """Test the copilot module."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.app = app.test_client()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_01(self):
        """Test the copilot module."""
        pass


# Path: test_copilot.py
if __name__ == '__main__':
    unittest.main()
