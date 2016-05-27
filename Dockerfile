FROM alexjpaz/letsencrypt-s3front-docker

RUN mkdir /app
WORKDIR /app
ADD main.py /app/main.py

ENTRYPOINT ["python", "main.py"]
