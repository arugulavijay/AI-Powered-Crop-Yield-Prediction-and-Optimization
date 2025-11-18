# High Risk Crop Popup Feature

## 🚨 High Risk Alert System

This feature automatically detects when a selected crop has high risk factors and displays a popup with safer alternatives.

## How It Works

### Automatic Risk Detection
- The system analyzes each crop selection based on location, soil type, and current conditions
- When overall risk is classified as "High", a popup automatically appears
- The popup shows only after the prediction results are loaded

### High-Risk Crops (for testing)
The following crops are configured to trigger high-risk alerts:
- **Cotton** ⚠️ High Risk
- **Sugarcane** ⚠️ High Risk  
- **Tobacco** ⚠️ High Risk
- **Chili** ⚠️ High Risk
- **Coffee** ⚠️ High Risk

### Medium-Risk Crops
- **Wheat** 🟡 Medium Risk
- **Maize** 🟡 Medium Risk
- **Soybean** 🟡 Medium Risk

### Low-Risk Crops
- **Rice** ✅ Low Risk
- **Pulses** ✅ Low Risk
- Other crops not listed above

## Testing the Feature

### Step 1: Select a High-Risk Crop
1. Open the application
2. Choose **Cotton** or **Sugarcane** from the crop selector
3. Fill in location (e.g., "Maharashtra")
4. Select soil type (e.g., "clay")
5. Enter land area (e.g., "5")
6. Click "Analyze"

### Step 2: Popup Appearance
- After analysis completes, the high-risk popup will automatically appear
- The popup displays:
  - ⚠️ Risk warning explanation
  - 📊 Safer crop alternatives with low/medium risk
  - 💰 Financial projections for each alternative
  - 📈 Suitability scores and market information

### Step 3: Choose Alternative
- Review the recommended alternatives
- Click "Switch to [Crop Name]" to automatically update your selection
- The form will update and re-run analysis with the new crop

### Step 4: Compare Results
- Notice how the new crop shows lower risk levels
- Compare financial projections and success factors
- The popup won't appear again for low/medium risk crops

## Popup Features

### Risk Analysis Details
- **Weather Risk**: Drought/flooding potential
- **Market Risk**: Price volatility and demand
- **Pest & Disease Risk**: Susceptibility factors
- **Soil Compatibility**: Match with selected soil type

### Alternative Recommendations
- **Suitability Score**: 0-100% compatibility rating
- **Expected Yield**: Projected output per acre
- **Profit Potential**: Estimated financial returns
- **Market Price**: Current market rates
- **Risk Level**: Low/Medium/High classification
- **Success Reasons**: Why this crop is recommended

### User Options
- **Switch Crop**: Automatically update selection and re-analyze
- **Continue with Original**: Proceed despite high risk
- **Close Popup**: Dismiss and review current analysis

## Technical Implementation

### Risk Calculation Logic
```typescript
const getRiskForCrop = (cropName: string): 'Low' | 'Medium' | 'High' => {
  const highRiskCrops = ['Cotton', 'Sugarcane', 'Tobacco', 'Chili', 'Coffee'];
  const mediumRiskCrops = ['Wheat', 'Maize', 'Soybean'];
  
  if (highRiskCrops.some(crop => cropName.toLowerCase().includes(crop.toLowerCase()))) {
    return 'High';
  } else if (mediumRiskCrops.some(crop => cropName.toLowerCase().includes(crop.toLowerCase()))) {
    return 'Medium';
  }
  return 'Low';
};
```

### Popup Trigger Condition
- Overall risk level = "High"
- Prediction results loaded successfully
- Popup hasn't been shown for current crop yet
- Loading state is complete

## Benefits for Farmers

### Risk Mitigation
- **Early Warning**: Alerts before investment
- **Alternative Options**: Provides safer choices
- **Data-Driven**: Based on comprehensive analysis

### Financial Protection
- **Loss Prevention**: Avoids high-risk investments
- **Better ROI**: Suggests more profitable options
- **Market Insights**: Current price and demand data

### Decision Support
- **Informed Choices**: Complete risk breakdown
- **Comparison Tools**: Side-by-side alternatives
- **Expert Recommendations**: Algorithm-based suggestions

## Future Enhancements

### Advanced Features
- **Custom Risk Thresholds**: User-defined risk tolerance
- **Historical Data**: Past performance trends
- **Weather Integration**: Real-time weather risk assessment
- **Insurance Recommendations**: Crop insurance suggestions
- **Expert Consultation**: Connect with agricultural advisors

### Smart Notifications
- **Seasonal Alerts**: Optimal planting time reminders
- **Market Updates**: Price change notifications
- **Weather Warnings**: Extreme weather alerts
- **Success Stories**: Farmer testimonials and case studies

---

## Quick Test Commands

1. **High Risk Test**: Select "Cotton" + any location/soil
2. **Medium Risk Test**: Select "Wheat" + any location/soil  
3. **Low Risk Test**: Select "Rice" + any location/soil

The popup will only appear for "Cotton" selection, demonstrating the high-risk detection system.