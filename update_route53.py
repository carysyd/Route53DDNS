#!/usr/bin/python3

# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
import argparse
import boto3
from requests import get

class DNSConfig:
    def __init__(self, domain_id, record):
        self.domain_id = domain_id
        self.record = record

def get_public_ip():
    ip = get('https://api.ipify.org').text
    return ip
    
def update_route53_record(route53_client, dns_config, new_ip):
    try :
        response = route53_client.change_resource_record_sets(
            HostedZoneId=dns_config.domain_id,
            ChangeBatch= {
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                        'Name': dns_config.record,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [{'Value': new_ip}]
                    }
                }]
        })
    except Exception as e:
        print(e)

def main():

    parser = argparse.ArgumentParser(description='Update Route53 DNS record')

    parser.add_argument('--AWSAccessKeyId', required=True, type=str)
    parser.add_argument('--AWSSecretKey', required=True, type=str)
    parser.add_argument('--HostedZoneId', required=True, type=str)
    parser.add_argument('--Record', required=True, type=str)

    args = parser.parse_args()

    public_ip = get_public_ip()
    print("Public IP address is: %s" % public_ip)

# aws_access_key_id='AKIA4GCRBDJI4TAO5I2G'
# aws_secret_access_key='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'

    client = boto3.client('route53',
        aws_access_key_id=args.AWSAccessKeyId,
        aws_secret_access_key=args.AWSSecretKey)

# dns_config = DNSConfig('/hostedzone/Z1NYRZ306RYBQD', 'caryli.com', 'vpn.caryli.com')
    dns_config = DNSConfig(args.HostedZoneId, args.Record)

    update_route53_record(client, dns_config, public_ip)

  
if __name__== "__main__":
  main()