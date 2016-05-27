import subprocess
import os
import boto3
import logging
import sys
import argparse

parser = argparse.ArgumentParser(description='Play some sounds')
parser.add_argument('--email',  required=True)
parser.add_argument('--domain',  required=True)
parser.add_argument('--website-bucket',  required=True)
parser.add_argument('--certs-bucket',required=True)
parser.add_argument('--region', required=True)
parser.add_argument('--cloudfront-id', required=True)
args = parser.parse_args()

# Global variables
email = args.email.strip()
domain_name = args.domain.strip()
s3_website_bucket = args.website_bucket.strip()
region = args.region.strip()
cloudfront_distribution_id = args.cloudfront_id.strip()
destination_s3_cert_bucket = args.certs_bucket.strip()
temp_dir = "/tmp"

# Open S3 connection and setup logger
s3_client = boto3.client('s3')

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():

    logger.info("Running letsencrypy.py")
    # Command line to execute to create/renew certificate
    command = "letsencrypt --agree-tos -a letsencrypt-s3front:auth --letsencrypt-s3front:auth-s3-bucket {} " \
              "--letsencrypt-s3front:auth-s3-region {} -i letsencrypt-s3front:installer " \
              "--letsencrypt-s3front:installer-cf-distribution-id {} -d {} --email {} --keep --config-dir {} " \
              "--work-dir {} --logs-dir {} --no-redirect --text --server https://acme-v01.api.letsencrypt.org/directory".format(s3_website_bucket, region,
                                                                        cloudfront_distribution_id, domain_name, email,
                                                                        temp_dir, temp_dir, temp_dir)

    # Execute command line and get results
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        logger.error("Failed to create/renew certificate. Error code: {}. Error output: {}".format(e.returncode, e.output))
    else:
        logger.info(output)

    # Copy off all resulting files to private S3 bucket
    for root, dirs, files in os.walk(temp_dir):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, temp_dir)
            destination_s3_path = os.path.join(relative_path)

            logger.info("Uploading {} to bucket {}".format(destination_s3_path, destination_s3_cert_bucket))
            s3_client.upload_file(local_path, destination_s3_cert_bucket, destination_s3_path)

    return "Completed"

if __name__ == "__main__":
    main()
