FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir \
    "streamlit>=1.66.1" \
    "joblib>=1.6.0" \
    "numpy>=2.4.6" \
    "pandas>=3.1.0" \
    "scikit-learn>=1.9.1"

COPY main.py ./
COPY models ./models

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]