FROM gliderlabs/alpine:3.3

RUN apk add --update \
      git \
      python \
      python-dev \
      py-pip \
      build-base \
      linux-headers \
      gcc \
      dialog \
      augeas-libs \
      openssl-dev \
      libffi-dev \
      ca-certificates \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN pip install letsencrypt
RUN pip install git+git://github.com/alexjpaz/certbot-s3front.git@master

CMD ["letsencrypt"]
