# Route53DDNS
Use Route53 as Dynamic DNS service, update public IP periodically.

## Building the docker image
Following is an example to build the docker image and tag `carysyd/route53ddns`

```sh
docker build -t carysyd/route53ddns .
```

This image is also published to [DockerHub carysyd/route53ddns](https://hub.docker.com/r/carysyd/route53ddns) if you want to use it directly.

## Running the application

DNS record update is idempotent. You may choose the following environments to run the application.

Four parameters are needed:
- AWSAccessKeyId - the AWS IAM user access key. This user needs to have access permission to update Route53 DNS records.
- AWSSecretKey - the AWS IAM user secret key
- HostedZoneId - the AWS Route53 record hosted zone id
- Record - the AWS Route53 record to be updated

### Run in Docker

Following is an example to supply an AWS credential and update the given DNS record in the AWS Host Zone.

```sh
docker run carysyd/route53ddns --HostedZoneId Z1NYRXXXXXXXXXX --Record vpn.somewhere.com
```

### Run in Kubernetes

Use Helm to install the application to a Kubernetes cluster.

TO DO: the AWS credentials are the base64 encoded strings. I'll update the repo with a better way to get the AWS credentials

```sh
helm upgrade -f values.yaml route53ddns .  --namespace route53ddns --create-namespace --set dns.hostedZoneId=Z1NXXXXXXXXXX --set dns.hostedZoneRecord=vpn.somewhere.com --set aws.accessKeyId="QUtXXXXXXXXXXXXXX=" --set aws.secretKey="YlBqcXXXXXXXXXXXXXXXXXXXXXXX=="
```
