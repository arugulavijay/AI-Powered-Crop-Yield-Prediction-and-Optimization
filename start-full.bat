@echo off
echo Starting Agro Predict Wise Full Application...

echo Installing/Updating Python dependencies...
cd backend
pip install -r requirements.txt
cd ..

echo Installing/Updating Node dependencies...
npm install

echo.
echo Starting both servers...
echo.

echo Starting Backend Server in new window...
start "Backend Server" /min cmd /c "cd backend && python app.py ^& pause"

timeout /t 5

echo Starting Frontend Server...
npm run dev

echo.
echo Application startup complete!
echo Backend API: http://localhost:3001
echo Frontend App: http://localhost:5173
echo.