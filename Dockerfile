FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD ["sh", "-c", "uvicorn app:app --host=0.0.0.0 --port=${PORT}"]
