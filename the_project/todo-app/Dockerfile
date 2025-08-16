FROM python:3.9-slim
WORKDIR /app
COPY app.py .
EXPOSE $PORT
# Run the application in unbuffered mode
CMD ["python", "-u","app.py"]
