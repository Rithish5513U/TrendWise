# TrendWise Frontend

Modern, responsive React application for the TrendWise inventory management platform, built with TypeScript, Vite, and Material-UI.

## ✨ Features

### User Interface
- **Modern Design**: Clean, professional UI with Material-UI components
- **Responsive Layout**: Fully responsive across desktop, tablet, and mobile
- **Dark Theme**: Beautiful gradient backgrounds and modern aesthetics
- **Interactive Charts**: Real-time data visualization with Recharts
- **Smooth Navigation**: Fast client-side routing with React Router

### Pages & Functionality

#### Public Pages
- **Landing Page**: Feature showcase with call-to-action
- **Login/Signup**: Authentication with JWT tokens

#### Protected Pages
- **Dashboard**: Overview with key metrics, charts, and quick actions
- **Inventory Management**: Product CRUD operations with search and filters
- **Sales Tracking**: Record sales with automatic inventory updates
- **Forecasting**: AI-powered demand predictions with visual charts
- **AI Chat**: Interactive chat with Gemini AI for business insights
- **AI Recommendations**: Smart suggestions for inventory optimization
- **Alert Settings**: Configure notifications for low stock and demand spikes
- **Billing**: Subscription plans and payment management

### State Management
- **Redux Toolkit**: Centralized state management
- **Persistent Auth**: Token stored in localStorage
- **Type Safety**: Full TypeScript support for reducers and actions

### API Integration
- **Axios Instance**: Configured HTTP client with interceptors
- **Auto Token Injection**: JWT automatically added to requests
- **Error Handling**: Global error interceptor for 401/403 responses
- **Proxy Configuration**: Development proxy to backend API

## 🛠️ Tech Stack

- **React** 19.2.0 - UI library
- **TypeScript** 5.9.3 - Type safety
- **Vite** 7.2.4 - Build tool and dev server
- **Material-UI** 6.3.0 - Component library
- **Redux Toolkit** 2.11.2 - State management
- **React Router** 7.1.4 - Routing
- **Recharts** 3.6.0 - Data visualization
- **Axios** 1.7.9 - HTTP client
- **Emotion** - CSS-in-JS styling

## 📁 Project Structure

```
frontend/
├── public/
│   └── vite.svg              # Favicon
├── src/
│   ├── api/
│   │   └── axios.ts          # Configured Axios instance
│   ├── assets/
│   │   ├── loginRight.png    # Auth page visual
│   │   └── react.svg
│   ├── components/
│   │   ├── AuthVisualPanel.tsx      # Auth page right panel
│   │   ├── DashboardNavbar.tsx      # Top navigation bar
│   │   ├── FeatureCard.tsx          # Landing page feature cards
│   │   ├── FlowerIcon.tsx           # Logo component
│   │   ├── GradientBackground.tsx   # Background wrapper
│   │   ├── Navbar.tsx               # Public page navbar
│   │   └── Sidebar.tsx              # Dashboard sidebar
│   ├── pages/
│   │   ├── AIRecommendationsPage.tsx
│   │   ├── AlertSettingsPage.tsx
│   │   ├── BillingPage.tsx
│   │   ├── ChatWithAIPage.tsx
│   │   ├── Dashboard.tsx
│   │   ├── ForecastingPage.tsx
│   │   ├── InventoryPage.tsx
│   │   ├── LandingPage.tsx
│   │   ├── LoginPage.tsx
│   │   ├── SalesPage.tsx
│   │   └── SignupPage.tsx
│   ├── store/
│   │   ├── authSlice.ts      # Authentication state
│   │   ├── hooks.ts          # Typed Redux hooks
│   │   └── index.ts          # Store configuration
│   ├── App.tsx               # Main app component
│   ├── App.css               # Global styles
│   ├── index.css             # Reset and base styles
│   ├── main.tsx              # App entry point
│   └── theme.ts              # MUI theme configuration
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts            # Vite configuration
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and npm
- Backend API running on `http://localhost:8080`

### Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure environment** (optional):
   Create `.env` file:
   ```env
   VITE_API_URL=http://localhost:8080
   ```

3. **Start development server**:
   ```bash
   npm run dev
   ```
   
   App runs on `http://localhost:3000`

### Available Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

## 🔧 Configuration

### Vite Config (`vite.config.ts`)

The app is configured with proxies for seamless API integration:

```typescript
server: {
  port: 3000,
  proxy: {
    '/api': 'http://localhost:8080',
    '/auth': 'http://localhost:8080',
    '/product': 'http://localhost:8080',
    '/sales': 'http://localhost:8080',
    '/billing': 'http://localhost:8080',
  }
}
```

### Material-UI Theme (`theme.ts`)

Custom theme with:
- Primary color palette
- Typography settings
- Component overrides
- Responsive breakpoints

### Redux Store (`store/index.ts`)

Configured with:
- Auth slice for user authentication
- Typed hooks (`useAppDispatch`, `useAppSelector`)
- Redux DevTools integration

## 🌐 API Integration

### Axios Configuration

```typescript
// Auto-inject JWT token
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle 401 errors globally
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login or show error
    }
    return Promise.reject(error);
  }
);
```

### Example API Call

```typescript
import axiosInstance from '../api/axios';

const fetchProducts = async () => {
  const response = await axiosInstance.get('/product');
  return response.data;
};
```

## 🎨 Styling Approach

- **MUI Components**: Pre-built, accessible components
- **Emotion CSS-in-JS**: Scoped styles with `sx` prop
- **Theme System**: Consistent colors, spacing, typography
- **Responsive Design**: Mobile-first approach with breakpoints

## 🚢 Deployment

### Vercel (Recommended)

1. **Connect GitHub repository**
2. **Framework Preset**: Vite
3. **Root Directory**: `frontend`
4. **Build Command**: `npm run build`
5. **Output Directory**: `dist`
6. **Environment Variables**: Add `VITE_API_URL` with your backend URL
7. **Deploy** 🚀

### Build Output

```bash
npm run build
```

Generates optimized production build in `dist/`:
- Minified JavaScript
- Optimized CSS
- Asset hashing for caching
- Tree-shaking for smaller bundle

## 🔐 Authentication Flow

1. User logs in via `/login`
2. Backend returns JWT token
3. Token stored in Redux store + localStorage
4. Axios interceptor adds token to all requests
5. Protected routes check `isAuthenticated` state
6. Logout clears token and redirects to landing

## 📊 Key Components

### Dashboard Layout
- **DashboardNavbar**: Top bar with user menu
- **Sidebar**: Navigation menu with icons
- **Content Area**: Main page content

### Reusable Components
- **FeatureCard**: Display feature with icon and description
- **GradientBackground**: Consistent background styling
- **FlowerIcon**: Brand logo component

## 🐛 Troubleshooting

**CORS Issues**: Ensure backend has CORS enabled for `http://localhost:3000`

**Proxy Not Working**: Restart Vite dev server after config changes

**Build Errors**: Clear `node_modules` and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

**Type Errors**: Ensure TypeScript version matches:
```bash
npm install typescript@~5.9.3
```

## 📝 Best Practices

- Use TypeScript for all new files
- Follow Material-UI theming for consistent design
- Keep components small and focused
- Use Redux for global state, local state for UI
- Implement error boundaries for production
- Add loading states for async operations
- Use React.memo for expensive renders

## 🔮 Future Enhancements

- [ ] Progressive Web App (PWA) support
- [ ] Offline mode with service workers
- [ ] Real-time updates with WebSockets
- [ ] Advanced filtering and search
- [ ] Export data to CSV/Excel
- [ ] Multi-language support (i18n)
- [ ] Accessibility improvements (WCAG 2.1)

## 📄 License

Private - TrendWise Platform

---

**Built with React ⚛️ + TypeScript 💙 + Material-UI 🎨**
