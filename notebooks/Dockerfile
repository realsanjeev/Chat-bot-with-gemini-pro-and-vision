FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements.txt first for better caching of dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port for Jupyter Notebook
EXPOSE 8888

# Start Jupyter Notebook when the container runs
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--allow-root"]

