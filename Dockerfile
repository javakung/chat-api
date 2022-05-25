FROM python:3.8

WORKDIR /

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY app /app
EXPOSE 8000

#CMD ["uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0", "--root-path", "/chat-api"]
CMD ["uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]