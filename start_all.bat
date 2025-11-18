@echo off
echo Starting Agro Predict Wise Application...

echo Starting Backend Server...
start "Backend" /D "agro-predict-wise-97-main\backend" cmd /k "python app.py"

timeout /t 10

echo Starting Frontend Server...
start "Frontend" /D "." cmd /k "npm run dev"

echo.
echo Both servers should now be running:
echo Backend: http://localhost:3001
echo Frontend: http://localhost:8080
echo.
echo You can also open test_frontend.html to test the backend APIs directly.
echo.
pause