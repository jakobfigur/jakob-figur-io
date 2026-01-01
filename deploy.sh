#!/bin/bash
set -e

echo "🚀 Starting deployment..."

# Configuration
CONTAINER_NAME="jakob-website"
IMAGE_NAME="jakob-figur-io"
PORT=8501

# Navigate to project directory
cd ~/jakob-figur-io

# Pull latest code
echo "📥 Pulling latest code from GitHub..."
git pull origin main

# Stop and remove existing container
echo "🛑 Stopping existing container..."
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

# Build new image
echo "🔨 Building Docker image..."
docker build -t $IMAGE_NAME .

# Run new container
echo "🐳 Starting new container..."
docker run -d \
  --name $CONTAINER_NAME \
  --restart unless-stopped \
  -p $PORT:8501 \
  $IMAGE_NAME

# Clean up old images
echo "🧹 Cleaning up old images..."
docker image prune -f

# Show status
echo ""
echo "✅ Deployment complete!"
echo "📍 Website accessible at: http://188.245.237.225:$PORT"
echo ""
docker ps | grep $CONTAINER_NAME
