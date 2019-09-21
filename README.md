# Route53DDNS
Use Route53 as Dynamic DNS service, update public IP periodically.

## Building the docker image
Following is an example to build the docker image and tag `carysyd/route53ddns`

```bash
docker build -t carysyd/route53ddns .
```

This image is also published to [DockerHub carysyd/route53ddns](https://hub.docker.com/r/carysyd/route53ddns) if you want to use it directly.
  
## Running the docker image
Following is an example to supply an AWS credential and update the given DNS record in the AWS Host Zone

```bash
docker run carysyd/route53ddns --AWSAccessKeyId AKIAXXXXXXXXXXXXX --AWSSecretKey 8VNdhwXXXXXXXXXXXXXXXXXX --HostedZoneId Z1NYRXXXXXXXXXX --Record vpn.somewhere.com
```

DNS record update is idempotent.

You will need to supply all 4 command line arguments
- AWSAccessKeyId - the AWS IAM user access key. This user needs to have access permission to update Route53 DNS records.
- AWSSecretKey - the AWS IAM user secret key
- HostedZoneId - the AWS Route53 record hosted zone id
- Record - the AWS Route53 record to be updated
