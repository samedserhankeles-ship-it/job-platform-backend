# Vercel Speed Insights Setup Guide

This job-platform-backend is configured to work with Vercel Speed Insights for monitoring frontend performance.

## What is Vercel Speed Insights?

Vercel Speed Insights is a performance monitoring tool that tracks Web Vitals metrics including:
- **Largest Contentful Paint (LCP)** - Loading performance
- **First Input Delay (FID)** - Interactivity
- **Cumulative Layout Shift (CLS)** - Visual stability

## Backend Configuration

The backend is already configured to serve static files and HTML with Speed Insights integration points. The main components are:

1. **Django settings** - CORS and static file configuration in `backend/settings.py`
2. **Templates** - Base HTML templates with Speed Insights script placeholders
3. **Home page** - `/` endpoint provides setup information
4. **Health check** - `/health/` endpoint for monitoring

## Frontend Integration

Since Vercel Speed Insights is a **client-side monitoring tool**, you need to integrate it in your frontend application:

### For Next.js Applications

1. **Install the package:**
   ```bash
   npm install @vercel/speed-insights
   # or
   pnpm add @vercel/speed-insights
   # or
   yarn add @vercel/speed-insights
   ```

2. **Import and use in your root layout or main component:**
   ```javascript
   import { SpeedInsights } from '@vercel/speed-insights/next'
   
   export default function RootLayout({
     children,
   }: {
     children: React.ReactNode
   }) {
     return (
       <html lang="en">
         <body>
           {children}
           <SpeedInsights />
         </body>
       </html>
     )
   }
   ```

### For React Applications

1. **Install the package:**
   ```bash
   npm install @vercel/speed-insights
   ```

2. **Inject Speed Insights in your main entry point:**
   ```javascript
   import { injectSpeedInsights } from '@vercel/speed-insights';
   
   injectSpeedInsights();
   
   import App from './App';
   ```

### For Plain HTML/JavaScript

Add this script tag directly to your HTML file:
```html
<script defer src="/_vercel/insights/script.js"></script>
```

### For Vue Applications

1. **Install the package:**
   ```bash
   npm install @vercel/speed-insights
   ```

2. **Use in your main.js:**
   ```javascript
   import { injectSpeedInsights } from '@vercel/speed-insights';
   
   injectSpeedInsights();
   
   import App from './App.vue'
   ```

### For Other Frameworks

Most frameworks support the injectable approach:
```javascript
import { injectSpeedInsights } from '@vercel/speed-insights';

injectSpeedInsights();
```

## Configuration

### Important Notes

- **Client-side only**: Speed Insights runs on the client side only. It collects Web Vitals from real users.
- **Production deployment**: Speed Insights data is only collected and sent when deployed on Vercel.
- **No API changes needed**: The backend API doesn't require modifications for Speed Insights to work.

### Environment Variables

Configure in your frontend `.env` or `.env.local`:
```
NEXT_PUBLIC_VERCEL_ENABLED=true
```

## Monitoring

Once integrated in your frontend:

1. Deploy your frontend to Vercel
2. Visit your Vercel project dashboard
3. Navigate to "Speed Insights" section
4. Monitor your Web Vitals metrics in real-time

## Documentation

For complete documentation and advanced configuration:
- [Vercel Speed Insights Documentation](https://vercel.com/docs/speed-insights)
- [@vercel/speed-insights NPM Package](https://www.npmjs.com/package/@vercel/speed-insights)

## Backend API Configuration

The backend is CORS-configured to work with frontends deployed on:
- Local development: `http://localhost:3000`
- Production: Configure via `CORS_ALLOWED_ORIGINS` environment variable

Example environment variable:
```
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://your-frontend.vercel.app
```

## Testing Locally

1. **Start the backend:**
   ```bash
   python manage.py runserver
   ```

2. **Access the home page:**
   - Open `http://localhost:8000/` to see setup information
   - Check `http://localhost:8000/health/` for API health status

3. **Connect your frontend:**
   - Point your frontend API calls to `http://localhost:8000`
   - Ensure CORS settings allow your frontend domain

## Deployment

When deploying to Vercel:

1. **Backend settings are pre-configured** in `vercel.json`
2. **Ensure environment variables are set** in your Vercel project
3. **Frontend will automatically collect metrics** once Speed Insights is integrated

For more help, refer to the [Vercel documentation](https://vercel.com/docs).
