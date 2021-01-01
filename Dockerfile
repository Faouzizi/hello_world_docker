FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org --requirement requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]