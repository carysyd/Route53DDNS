FROM python:3-alpine

RUN pip3 install boto3 requests

ADD update_route53.py /root

ENTRYPOINT ["python3", "/root/update_route53.py"]