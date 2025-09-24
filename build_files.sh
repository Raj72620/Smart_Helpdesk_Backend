#!/bin/bash

# Install Python dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Make migrations and migrate
echo "Making migrations..."
python3 manage.py makemigrations
echo "Applying migrations..."
python3 manage.py migrate
