FROM python:3.9-alpine
RUN pip install requests
WORKDIR /app
COPY *.py /app/
CMD ["python", "app.py"]