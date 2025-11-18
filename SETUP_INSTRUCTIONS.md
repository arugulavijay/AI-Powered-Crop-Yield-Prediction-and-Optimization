# Setup Instructions for Agro Predict Wise

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.8 or higher
- Node.js 16 or higher
- npm (comes with Node.js)

## Step 1: Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - Create a copy of `.env.example` as `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file and replace the placeholder values with your actual API keys:
     - `GOOGLE_MAPS_API_KEY`: Get from Google Cloud Console
     - `OPENWEATHER_API_KEY`: Get from OpenWeatherMap

## Step 2: Frontend Setup

1. From the root directory, install frontend dependencies:
   ```bash
   npm install
   ```

## Step 3: Running the Application

You have two options to run the application:

### Option 1: Run servers separately

1. Start the backend server:
   ```bash
   cd backend
   python app.py
   ```

2. In a new terminal, start the frontend:
   ```bash
   npm run dev
   ```

### Option 2: Run both servers together

From the root directory:
```bash
npm run dev:full
```

This will start both the Flask backend (on port 3001) and the Vite frontend (on port 5173).

## Accessing the Application

Once both servers are running:
- Open your browser and go to `http://localhost:5173`
- The application should load and connect to the backend API

## Troubleshooting

### API Key Issues

If you see errors about API keys:
1. Make sure you've created a `.env` file in the `backend` directory
2. Verify your API keys are correct
3. Ensure the required APIs are enabled in your Google Cloud project:
   - Geocoding API
   - Places API

### Port Conflicts

If port 3001 or 5173 is already in use:
1. Edit `backend/app.py` to change the port:
   ```python
   if __name__ == '__main__':
       app.run(debug=True, port=YOUR_PREFERRED_PORT)
   ```
2. Update `frontend/.env` to match the new backend port:
   ```
   VITE_API_BASE_URL=http://localhost:YOUR_PREFERRED_PORT/api
   ```

### Dependency Issues

If you encounter dependency issues:
1. Try upgrading pip:
   ```bash
   pip install --upgrade pip
   ```
2. Reinstall dependencies:
   ```bash
   pip install -r backend/requirements.txt
   npm install
   ```

## API Endpoints

The backend provides the following API endpoints:

### Weather Services
- `GET /api/weather/current` - Get current weather for a location
- `GET /api/weather/forecast` - Get weather forecast for a location
- `GET /api/weather/coordinates` - Get weather by coordinates
- `GET /api/weather/agricultural` - Get agricultural weather insights

### Location Services
- `GET /api/location/geocode` - Geocode a location name to coordinates
- `GET /api/location/reverse` - Reverse geocode coordinates to location
- `GET /api/location/search` - Search for locations by name

### Agricultural Services
- `POST /api/agricultural/risk-analysis` - Analyze agricultural risks
- `POST /api/agricultural/recommendations` - Get crop recommendations

### Health Check
- `GET /api/health` - Check if the service is running

## Getting API Keys

### Google Maps API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - Geocoding API
   - Places API
   - Maps JavaScript API
4. Create credentials (API Key)
5. Update the `backend/.env` file with your API key

### OpenWeatherMap API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key from the "API keys" section
4. Update the `backend/.env` file with your API key