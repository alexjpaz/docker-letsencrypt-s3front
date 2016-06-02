# letsencrypt-s3front:

Adapated script from https://vittegleo.com/blog/letsencrypt-lambda-function/

# Usage

```
docker run \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID" \
  letsencrypt-s3front-docker \
  --email $EMAIL \
  --domain $DOMAIN \
  --website-bucket $WEBSITE_BUCKET \
  --certs-bucket $CERTS_BUCKET \
  --cloudfront-id $CLOUDFRONT_ID \
  --region $REGION
```
