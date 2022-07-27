FROM google/cloud-sdk:392.0.0-slim

RUN pip3 install fastapi uvicorn

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
