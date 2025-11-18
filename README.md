# Agro Predict Wise

An intelligent agricultural prediction and recommendation system that helps farmers make data-driven decisions about crop selection, risk assessment, and farming practices based on real-time weather data and location-specific insights.

## Features

- Real-time weather data integration
- Location-based agricultural recommendations
- Crop risk analysis
- Soil compatibility assessment
- Market insights and pricing information
- Multi-language support

## Tech Stack

### Frontend
- React with TypeScript
- Vite build tool
- Tailwind CSS for styling
- Shadcn/ui components
- React Router for navigation

### Backend
- Flask (Python)
- Google Maps API
- OpenWeatherMap API
- RESTful API architecture

## Prerequisites

- Node.js (v16 or higher)
- Python (3.8 or higher)
- npm or yarn package manager

## Setup Instructions

### 1. Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Set up environment variables by creating a `.env` file:
```env
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
OPENWEATHER_API_KEY=your_openweathermap_api_key_here
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
```

Start the backend server:
```bash
python app.py
```

The backend will run on `http://localhost:3001`

### 2. Frontend Setup

From the root directory, install dependencies:
```bash
npm install
```

Start the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

### 3. Running Both Servers Together

You can also start both servers with a single command:
```bash
npm run dev:full
```

This will run the Python script that starts both the Flask backend and Vite frontend simultaneously.

## API Documentation

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

## Project Structure

```
agro-predict-wise/
├── backend/                 # Flask backend
│   ├── app.py              # Main application
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
├── src/                   # Frontend source code
│   ├── components/        # React components
│   ├── pages/             # Page components
│   ├── services/          # API service layer
│   ├── contexts/          # React contexts
│   ├── hooks/             # Custom hooks
│   ├── lib/               # Utility functions
│   └── data/              # Static data
├── public/                # Static assets
└── index.html            # Main HTML file
```

## Development

### Frontend Development

The frontend is built with React and TypeScript. Components are organized in the `src/components` directory.

### Backend Development

The backend is a Flask application that provides RESTful APIs for the frontend. All API routes are defined in `backend/app.py`.

## Deployment

### Backend Deployment

For production deployment, use a WSGI server like Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:3001 app:app
```

### Frontend Deployment

Build the production version:
```bash
npm run build
```

The built files will be in the `dist/` directory and can be served by any static file server.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue on the GitHub repository.