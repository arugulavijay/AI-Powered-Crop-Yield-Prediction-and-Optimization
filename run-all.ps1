# Agro Predict Wise - Run All Services
Write-Host "🌱 Starting Agro Predict Wise Application..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

# Start Backend in background job
Write-Host "🚀 Starting Backend Server..." -ForegroundColor Cyan
Start-Job -ScriptBlock {
    Set-Location "backend"
    python app.py
} -Name "BackendServer"

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Start Frontend
Write-Host "🚀 Starting Frontend Server..." -ForegroundColor Cyan
npm run dev

# Clean up jobs when finished
Get-Job | Remove-Job -Force