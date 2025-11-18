import sys
try:
    import flask
    import googlemaps
    import requests
    import os
    from dotenv import load_dotenv
    print("All Python dependencies are installed successfully!")
    print(f"Python version: {sys.version}")
    print(f"Flask version: {flask.__version__}")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"Error: {e}")