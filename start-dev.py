#!/usr/bin/env python3
"""
Development server starter script for Agro Predict Wise
Runs both frontend (Vite) and backend (Flask) servers simultaneously
"""

import subprocess
import sys
import os
import signal
import threading

# Global variables to track processes
frontend_process = None
backend_process = None
processes = []

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n\n🛑 Shutting down development servers...")
    for process in processes:
        try:
            process.terminate()
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(f"Error terminating process: {e}")
    
    print("✅ Development servers stopped.")
    sys.exit(0)

def start_frontend():
    """Start the Vite frontend development server"""
    global frontend_process
    print("🚀 Starting frontend development server...")
    try:
        frontend_process = subprocess.Popen(
            ["npm", "run", "dev"],
            cwd=os.getcwd(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        processes.append(frontend_process)
        
        # Print frontend output
        for line in iter(frontend_process.stdout.readline, ''):
            print(f"[Frontend] {line.rstrip()}")
            
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")

def start_backend():
    """Start the Flask backend server"""
    global backend_process
    print("🚀 Starting backend server...")
    try:
        backend_process = subprocess.Popen(
            ["python", "backend/app.py"],
            cwd=os.getcwd(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        processes.append(backend_process)
        
        # Print backend output
        for line in iter(backend_process.stdout.readline, ''):
            print(f"[Backend] {line.rstrip()}")
            
    except Exception as e:
        print(f"❌ Error starting backend: {e}")

def main():
    """Main function to start both servers"""
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    print("🌱 Agro Predict Wise Development Environment")
    print("=" * 50)
    
    # Check if required files exist
    if not os.path.exists("package.json"):
        print("❌ Error: package.json not found. Are you in the project root?")
        sys.exit(1)
        
    if not os.path.exists("backend/app.py"):
        print("❌ Error: backend/app.py not found.")
        sys.exit(1)
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=start_backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Start frontend in main thread
    start_frontend()
    
    # Wait for processes to complete
    for process in processes:
        process.wait()

if __name__ == "__main__":
    main()