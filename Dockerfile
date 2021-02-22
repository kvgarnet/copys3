FROM python:3.6
RUN pip install awscli boto3
WORKDIR /code
COPY ./ .
# command to run on container start
# CMD [ "python", "./copys3.py", "kvsource","kvdest","3"]
ENTRYPOINT [ "python", "./copys3.py" ]
CMD [ "kvsource","kvdest","1.5"]
