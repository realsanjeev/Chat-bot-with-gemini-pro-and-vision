## Tool (Function) Calling Using LLM

Large Language Models (LLMs) are excellent at generating human-like responses based on their training data. However, real-world applications often require **up-to-date**, **precise**, or **domain-specific** information that an LLM alone cannot reliably provide. For example:

* performing accurate calculations
* retrieving the latest information from the web
* accessing private databases or APIs
* interacting with external software, files, or systems

Since an LLM cannot inherently know real-time information or execute external actions, this leads to limitations.

**Tool calling** solves this problem.
It allows the LLM to invoke external functions, scripts, APIs, or tools when needed—essentially giving the model *superpowers* beyond text generation. Instead of relying only on its internal knowledge, the LLM can:

* run Python functions
* execute shell commands
* query search engines
* call third-party APIs
* or perform any custom operation you define

This makes the LLM far more reliable, practical, and usable for real-world tasks.

---

### Running the Script Inside a Docker Container

To demonstrate tool calling, we’ll create a simple tool that dynamically generates a script, executes it, and exposes it to the LLM. Because running bash commands can be unsafe on the host system, we execute everything inside a sandboxed environment for better isolation and consistency.

We’ll use a Docker container that launches a Jupyter Notebook server on the default port **8888**, and expose this port so it’s accessible from your host system.

**1. Create a `Dockerfile`**

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

**2. Build the Docker Image**

```bash
docker build -t my-jupyter-image .
```

**3. Run the Container**

```bash
docker run -it --rm -p 8888:8888 my-jupyter-image
```
