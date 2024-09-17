FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]