# TrendWise Backend API

Flask-based REST API for TrendWise - an AI-powered inventory management and forecasting platform.

## Features

- **Authentication**: JWT-based user authentication and authorization
- **Product Management**: CRUD operations for inventory items
- **Sales Tracking**: Record and analyze sales data
- **AI Forecasting**: Machine learning-powered demand forecasting using LightGBM
- **Smart Alerts**: Automated notifications for low stock and inventory insights
- **Billing System**: Subscription and payment management
- **AI Chat**: Integration with Google Gemini for intelligent recommendations

## Tech Stack

- **Framework**: Flask
- **Authentication**: Flask-JWT-Extended
- **Database**: MySQL (via PyMySQL)
- **Machine Learning**: LightGBM, scikit-learn, pandas, numpy
- **AI**: Google Gemini API
- **Server**: Gunicorn (production)

## Project Structure

```
backend/
├── src/
│   ├── app.py              # Main application entry point
│   ├── config.py           # Configuration management
│   ├── db.py               # Database connection
│   ├── extensions.py       # Flask extensions
│   ├── auth/              # Authentication endpoints
│   ├── product/           # Product management
│   ├── sales/             # Sales tracking
│   ├── forecast/          # ML forecasting
│   ├── alerts/            # Alert system
│   └── billing/           # Billing management
├── requirements.txt        # Python dependencies
├── Procfile               # Render deployment config
└── README.md              # This file
```

## Environment Variables

Create a `.env` file in the backend directory:

```env
# JWT Configuration
JWT_SECRET_KEY=your-secret-key-here
JWT_ACCESS_EXPIRES=3600

# MySQL Database
MYSQL_HOST=your-mysql-host
MYSQL_USERNAME=your-username
MYSQL_PASSWORD=your-password
MYSQL_PORT=3306
MYSQL_DATABASE=trendwise_db

# Google Gemini AI
GEMINI_API_KEY=your-gemini-api-key

# Email Configuration (for alerts)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password

# MongoDB (optional)
MONGO_URI=your-mongodb-uri
```

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   - Create `.env` file with required variables
   - Configure MySQL database connection

3. **Run the development server**:
   ```bash
   python src/app.py
   ```
   
   Server runs on `http://localhost:8080`

## Deployment to Render

1. **Push code to GitHub** (monorepo structure supported)

2. **Create Web Service on Render**:
   - Connect your GitHub repository
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn src.app:app`
   - **Environment**: Python 3

3. **Add Environment Variables**:
   - Go to Environment tab in Render dashboard
   - Add all variables from `.env` file
   - Set `PYTHON_VERSION` to `3.11` (or your preferred version)

4. **Database Setup**:
   - Create a MySQL database (Render, PlanetScale, or other)
   - Add database credentials to environment variables

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/profile` - Get user profile (protected)

### Products
- `GET /products` - List all products
- `POST /products` - Create new product
- `GET /products/:id` - Get product details
- `PUT /products/:id` - Update product
- `DELETE /products/:id` - Delete product

### Sales
- `GET /sales` - Get sales data
- `POST /sales` - Record new sale

### Forecasting
- `POST /forecast` - Generate demand forecast
- `GET /forecast/:product_id` - Get product forecast

### Alerts
- `GET /alerts` - Get alert settings
- `POST /alerts` - Configure alerts

### Billing
- `GET /billing` - Get billing information
- `POST /billing/subscribe` - Subscribe to plan

## Production Considerations

- **Database**: Use managed MySQL (e.g., PlanetScale, Render PostgreSQL, AWS RDS)
- **Environment Variables**: Never commit `.env` file
- **CORS**: Configure allowed origins in production
- **Security**: Use strong JWT secret keys
- **Logging**: Implement proper logging for debugging
- **Rate Limiting**: Add rate limiting for API endpoints
- **Monitoring**: Set up health checks and monitoring

## License

Private - TrendWise Platform
