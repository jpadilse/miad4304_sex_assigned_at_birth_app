# Use a specific base image version for better reproducibility
FROM python:3.10.11-slim-bullseye

# Add metadata labels
LABEL maintainer="j.padillas@uniandes.edu.co"
LABEL description="Streamlit application container"
LABEL version="1.0"

# Set working directory
WORKDIR /app

# Combine RUN commands to reduce layers and set up apt-get properly
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        software-properties-common \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && git clone --depth 1 https://github.com/jpadilse/miad4304_sex_assigned_at_birth_app.git . \
    && pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Expose port
EXPOSE ${STREAMLIT_SERVER_PORT}

# Add healthcheck with timeout and interval
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:${STREAMLIT_SERVER_PORT}/_stcore/health || exit 1

# Use array syntax for entrypoint
ENTRYPOINT ["streamlit", "run", "🚻_Inicio.py", \
            "--server.port=${STREAMLIT_SERVER_PORT}", \
            "--server.address=${STREAMLIT_SERVER_ADDRESS}"]