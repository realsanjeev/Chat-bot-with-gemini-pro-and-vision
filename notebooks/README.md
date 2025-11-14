### Running the Script Inside a Docker Container

Since the script executes bash commands directly, it’s safer and more consistent to run it inside an isolated sandbox environment.

We’ll use a Docker container that launches a Jupyter Notebook server on the default port **8888**, and expose this port so it’s accessible from your host system.

---

### 1. Create a `Dockerfile`

```Dockerfile
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose Jupyter Notebook port
EXPOSE 8888

# Launch Jupyter Notebook on container start
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--allow-root"]
```

---

### 2. Build the Docker Image

```bash
docker build -t my-jupyter-image .
```

---

### 3. Run the Container

```bash
docker run -it --rm -p 8888:8888 my-jupyter-image
```

---

This will start the Jupyter server inside the Docker container and make it available at `http://localhost:8888` on your host system.

