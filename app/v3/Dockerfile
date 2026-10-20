# Start from a small official Python image
FROM python:3.12-slim
# Work inside /app in the container
WORKDIR /app
# Install the libraries first (this layer is cached between builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the app code
COPY app.py .
# The app listens on port 5000
EXPOSE 5000
# Start the app
CMD ["python", "app.py"]
