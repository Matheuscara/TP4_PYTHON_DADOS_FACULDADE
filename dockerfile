FROM python:3.11-slim
	
WORKDIR /app
	
COPY . /app
	
RUN pip install --no-cache-dir pandas

CMD ["python", "src/main.py"]
