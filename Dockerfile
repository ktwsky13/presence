FROM 3.9.16-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "script.py"]
