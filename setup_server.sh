#!/bin/bash

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing Docker..."
sudo apt install -y docker.io

echo "Installing Nginx..."
sudo apt install -y nginx

echo "Enabling and starting Docker & Nginx..."
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl enable nginx
sudo systemctl start nginx

echo "Adding user to Docker group (you may need to log out and log back in)..."
sudo usermod -aG docker $USER

echo "Checking service status..."
echo "Docker status:"
sudo systemctl status docker --no-pager

echo "Nginx status:"
sudo systemctl status nginx --no-pager

echo "Server setup complete!"
