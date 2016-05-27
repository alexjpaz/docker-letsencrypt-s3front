# letsencrypt-s3front-docker:


# Usage

```
docker run \
  -e AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY" \
  -e AWS_SECRET_ACCESS_KEY="$AWS_ACCESS_KEY" \
  letsencrypt-s3front-docker \
  --email $EMAIL \
  --domain $DOMAIN \
  --website-bucket $WEBSITE_BUCKET \
  --certs-bucket $CERTS_BUCKET \
  --cloudfront-id $CLOUDFRONT_ID \
  --region $REGION
```
