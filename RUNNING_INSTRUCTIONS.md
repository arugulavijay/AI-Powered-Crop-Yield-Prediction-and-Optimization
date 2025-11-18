# Running Agro Predict Wise Application

## Prerequisites
- Python 3.7 or higher
- Node.js and npm
- Valid API keys for Google Maps and OpenWeatherMap

## Setup Instructions

1. **Install Backend Dependencies:**
   ```bash
   cd agro-predict-wise-97-main/backend
   pip install -r requirements.txt
   ```

2. **Configure API Keys:**
   - Copy `.env.example` to `.env`
   - Add your Google Maps API key and OpenWeatherMap API key to the `.env` file

3. **Start Backend Server:**
   ```bash
   cd agro-predict-wise-97-main/backend
   python app.py
   ```
   The backend will run on http://localhost:3001

4. **Install Frontend Dependencies:**
   ```bash
   npm install
   ```

5. **Start Frontend Development Server:**
   ```bash
   npm run dev
   ```
   The frontend will run on http://localhost:8080

## Alternative Method

You can also use the provided batch file to start both servers:
- Double-click on `start_all.bat`

## Testing the Application

1. **Backend Health Check:**
   Visit http://localhost:3001/api/health

2. **Test Frontend:**
   Visit http://localhost:8080

3. **Direct API Testing:**
   Open `test_frontend.html` in your browser to test backend APIs directly

## API Endpoints

- `GET /api/health` - Check if backend is running
- `GET /api/weather/current?location={location}` - Get current weather
- `POST /api/predict/crop` - Get crop predictions
- `GET /api/location/coordinates?location={location}` - Get coordinates for a location
- `GET /api/location/reverse?lat={lat}&lng={lng}` - Get location name from coordinates
- `GET /api/location/search?query={query}` - Search for locations
- `POST /api/analysis/agricultural` - Get agricultural insights
- `POST /api/analysis/financial` - Get financial analysis
- `GET /api/recommendations/fertilizer?crop={crop}&soil={soil}` - Get fertilizer recommendations
- `GET /api/calendar/seasonal?crop={crop}&location={location}` - Get seasonal calendar

## Troubleshooting

1. **Invalid API Keys:**
   - Ensure you have valid API keys for Google Maps and OpenWeatherMap
   - Check that the keys are correctly added to the `.env` file

2. **Port Conflicts:**
   - If port 3001 or 8080 is already in use, you can change the ports in the configuration

3. **Missing Dependencies:**
   - Make sure all dependencies are installed using `pip install -r requirements.txt` and `npm install`