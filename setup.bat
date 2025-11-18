@echo off
echo Agro Predict Wise - Setup Script
echo =================================

echo Installing frontend dependencies...
npm install

echo Installing backend dependencies...
cd backend
pip install -r requirements.txt
cd ..

echo.
echo Setup complete!
echo.
echo To run the development servers:
echo 1. Configure your API keys in backend/.env
echo 2. Run 'npm run dev:full' to start both frontend and backend
echo.