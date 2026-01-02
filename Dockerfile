# Build stage
FROM node:20-slim AS builder

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Build the Astro site
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built static files from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 8501 (to match existing server setup)
EXPOSE 8501

# Health check
HEALTHCHECK CMD wget --quiet --tries=1 --spider http://localhost:8501/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
