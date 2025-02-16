
FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "stonepaperscissor.wsgi:application", "--bind", "0.0.0.0:8000"]
