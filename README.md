# Basic Python Web App with Docker

This project shows how to run a basic Python web application inside a Docker container.

## Prerequisites

- Python 3.10+
- Docker Desktop (or Docker Engine)

## Example Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 1) Create a Simple Python Web App

Create `app.py`:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
		return "Hello from Python + Docker!"


if __name__ == "__main__":
		app.run(host="0.0.0.0", port=5000)
```

Create or update `requirements.txt`:

```text
flask==3.0.3
```

## 2) Add a Dockerfile

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## 3) Build the Docker Image

```bash
docker build -t basic-python-webapp .
```

## 4) Run the Container

```bash
docker run --rm -p 5000:5000 basic-python-webapp
```

Open your browser at:

```text
http://localhost:5000
```

## Optional: Run Without Docker

```bash
pip install -r requirements.txt
python app.py
```

## Run Tests

```bash
pytest -q
```

## Troubleshooting

- If port 5000 is busy, map a different port, for example:
	- `docker run --rm -p 8080:5000 basic-python-webapp`
- If Docker build fails on dependencies, ensure internet access and retry the build.

## License

This repository is provided under the license in `LICENSE`.

Adding code in develop brach 
