# Use the official Streamlit image as base
FROM streamlit/streamlit:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY app.py /app
COPY requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "--server.enableCORS", "false", "app.py"]
