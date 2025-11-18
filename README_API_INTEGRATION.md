# Backend Integration Guide

This document explains how to connect this frontend application to a backend API.

## 🔧 Setup

### 1. Environment Configuration

Copy `.env.example` to `.env` and configure your API endpoints:

```bash
cp .env.example .env
```

Edit `.env`:
```env
# Set your backend API URL
VITE_API_BASE_URL=http://localhost:3001/api

# Disable mock data to use real API
VITE_ENABLE_MOCK_DATA=false

# Optional: Add external API keys
VITE_OPENWEATHER_API_KEY=your_api_key_here
```

### 2. Backend API Requirements

Your backend should implement the following REST API endpoints:

#### Weather Service Endpoints
```
GET /api/weather/current?location={location}
GET /api/weather/forecast?location={location}&days={days}
GET /api/weather/coordinates?lat={lat}&lon={lon}
GET /api/weather/agricultural?location={location}&crop={crop}
GET /api/location/reverse?lat={lat}&lon={lon}
GET /api/location/search?q={query}
```

#### Market Service Endpoints
```
GET /api/market/prices?crops={crops}&location={location}
GET /api/market/crop-price?crop={crop}&location={location}
GET /api/market/summary?location={location}
GET /api/market/price-history?crop={crop}&period={period}&location={location}
GET /api/market/commodity?crop={crop}
GET /api/market/nearby?location={location}&radius={radius}
GET /api/market/price-alerts?userId={userId}
POST /api/market/price-alerts
```

#### Prediction Service Endpoints
```
POST /api/predictions/analyze
POST /api/predictions/risk-analysis
POST /api/predictions/yield
POST /api/predictions/financial
POST /api/predictions/recommendations
GET /api/predictions/seasonal-calendar?location={location}&crop={crop}
GET /api/predictions/cultivation-guide?crop={crop}&acres={acres}&location={location}
POST /api/predictions/feedback
```

#### Feedback Service Endpoints
```
POST /api/feedback/submit
POST /api/feedback/survey
POST /api/feedback/contact
POST /api/feedback/newsletter
GET /api/feedback/profile/{userId}
POST /api/feedback/profile
PUT /api/feedback/profile/{userId}
GET /api/feedback/analytics?timeframe={timeframe}
GET /api/feedback/engagement
POST /api/feedback/bug-report
POST /api/feedback/feature-request
```

## 📋 API Response Formats

### Standard API Response
```typescript
{
  success: boolean;
  data: T;
  message?: string;
  error?: string;
}
```

### Weather Data
```typescript
{
  temperature: number;
  humidity: number;
  windSpeed: number;
  condition: string;
  rainfall: number;
  location: string;
  icon?: string;
  feelsLike?: number;
  visibility?: number;
  uvIndex?: number;
  pressure?: number;
}
```

### Market Price Data
```typescript
{
  crop: string;
  currentPrice: number;
  previousPrice: number;
  change: number;
  changePercent: number;
  market: string;
  lastUpdated: string;
  demand: 'High' | 'Medium' | 'Low';
  quality: string;
  unit: string;
  currency: string;
}
```

### Prediction Result
```typescript
{
  input: PredictionInput;
  riskAnalysis: RiskAnalysis;
  yieldPrediction: YieldPrediction;
  financialAnalysis: FinancialAnalysis;
  recommendations: CropRecommendation[];
  insights: {
    bestPlantingTime: string;
    harvestTime: string;
    criticalPeriods: string[];
    successFactors: string[];
    commonChallenges: string[];
  };
  confidence: number;
  lastUpdated: string;
}
```

## 🚀 Development Mode

To run with mock data (for development without backend):

```env
VITE_ENABLE_MOCK_DATA=true
```

To run with real API:

```env
VITE_ENABLE_MOCK_DATA=false
VITE_API_BASE_URL=http://your-backend-url/api
```

## 🔄 Fallback Behavior

The application is designed with graceful fallback:

1. **API Available**: Uses real backend data
2. **API Unavailable**: Automatically falls back to mock data
3. **Offline**: Shows cached data with appropriate notifications

## 📦 Backend Technology Suggestions

### Recommended Tech Stack:
- **Node.js + Express** for REST API
- **Python + FastAPI** for ML predictions
- **PostgreSQL** for data storage
- **Redis** for caching
- **Docker** for containerization

### Sample Backend Structure:
```
backend/
├── src/
│   ├── controllers/
│   │   ├── weatherController.js
│   │   ├── marketController.js
│   │   ├── predictionController.js
│   │   └── feedbackController.js
│   ├── services/
│   │   ├── weatherService.js
│   │   ├── marketService.js
│   │   ├── mlService.js
│   │   └── feedbackService.js
│   ├── models/
│   │   ├── User.js
│   │   ├── Feedback.js
│   │   └── Prediction.js
│   ├── routes/
│   │   ├── weather.js
│   │   ├── market.js
│   │   ├── predictions.js
│   │   └── feedback.js
│   └── app.js
├── package.json
└── README.md
```

## 🔐 Authentication (Optional)

To add authentication, modify the API client in `src/services/api.ts`:

```typescript
// Set auth token
apiClient.setAuthToken('your-jwt-token');

// Remove auth token
apiClient.removeAuthToken();
```

## 📊 External Integrations

### Weather APIs:
- OpenWeatherMap
- WeatherAPI
- AccuWeather

### Market Data:
- Agricultural commodity exchanges
- Government agricultural departments
- Market data providers

### ML Services:
- Your custom ML models
- Google Cloud AI
- AWS SageMaker
- Azure ML

## 🐛 Error Handling

The frontend includes comprehensive error handling:

- **Network errors**: Automatic retry with exponential backoff
- **API errors**: User-friendly error messages
- **Offline mode**: Cached data display
- **Fallback data**: Mock data when API is unavailable

## 📈 Monitoring

Consider implementing:
- API response time monitoring
- Error rate tracking
- User analytics
- Performance metrics

## 🚀 Deployment

### Frontend Deployment:
```bash
npm run build
# Deploy to Vercel, Netlify, or your preferred hosting
```

### Environment Variables for Production:
```env
VITE_API_BASE_URL=https://your-production-api.com/api
VITE_ENABLE_MOCK_DATA=false
VITE_DEBUG_MODE=false
```

## 📞 Support

For issues with the integration:
1. Check the browser console for API errors
2. Verify environment variables are set correctly
3. Test API endpoints with tools like Postman
4. Review network requests in browser DevTools

The application will gracefully handle API failures and continue to function with mock data.