#!/bin/bash
set -e  # Exit on error

echo "========================================="
echo "Starting BookVerse on Railway..."
echo "========================================="

# Debug: Show environment
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Files in current directory:"
ls -la

# Check if app directory exists
if [ ! -d "app" ]; then
    echo "ERROR: 'app' directory not found!"
    echo "Contents of current directory:"
    ls -la
    exit 1
fi

# Create storage directories
mkdir -p storage/books storage/covers
echo "✓ Created storage directories"

# Run database migrations
echo "Running database migrations..."
if [ -f "alembic.ini" ]; then
    alembic upgrade head || echo "⚠ Migration warning (may be first deploy)"
else
    echo "⚠ alembic.ini not found, skipping migrations"
fi

# Add current directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)"
echo "PYTHONPATH set to: $PYTHONPATH"

# Start the application
echo "========================================="
echo "Starting Gunicorn server on port ${PORT:-8000}..."
echo "========================================="
exec gunicorn app.main:app \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 1 \
    --timeout 300 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    --preload

