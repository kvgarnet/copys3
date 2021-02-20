FROM python:3.6
RUN pip install awscli boto3
# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
#RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./ .

# command to run on container start
# CMD [ "python", "./copys3.py", "kvsource","kvdest","3"]
ENTRYPOINT [ "python", "./copys3.py" ]
CMD [ "kvsource","kvdest","3"]
