FROM alexjpaz/letsencrypt-s3front:0.1.1-base

RUN mkdir /app
WORKDIR /app
ADD main.py /app/main.py

ENTRYPOINT ["python", "main.py"]
