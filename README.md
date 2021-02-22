


<p align="center">
  
  <h3 align="center">CopyS3</h3>

  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#what-is-copys3">What is CopyS3</a>
     </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
 </ol>
</details>



## What is CopyS3
It is a Docker containerized Python application. 
When given the names of two S3 buckets (source, destination) and a threshold size (in MB), application will copy
all files greater than the specified threshold size from the source bucket to the destination bucket.
Assumptions are that the buckets are in the same region.


<!-- GETTING STARTED -->
## Getting Started

The application is built with AWS python SDK boto3 module, interacting with AWS S3 service

### Prerequisites
- A Linux host server for below tools installation
- [AWS Account](https://aws.amazon.com/free/?nc2=h_ql_pr) - free tier can be utilized for this exercise since all we need are (2) S3 buckets
  - [AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
- [Docker](https://docs.docker.com/install/)  - Install latest docker for your operating system.
- [Python](https://www.python.org)  - please use Python 3.6.x or greater if you decide to use Python
  - [AWS SDK Python boto3](https://aws.amazon.com/sdk-for-python/) - ensure boto3 installed on host server
- Create IAM user with AWSS3fullaccess permission. record user's AK/SK credentials
- Configure AK/SK via 'aws configure' on host server
- Verify that user has permission  with S3
```
aws s3 ls
```

### Installation
After above prerequisites tools installed on Linux Servers, please configure as below:

1. Clone the repo
   ```sh
   git clone https://github.com/kvgarnet/copys3.git
   ```
2. create S3 buckets (optional if you already created S3 buckets)
```
make mb
#Note:by default it will create buckets 'kvsource' 'kvdest', can also set your bucket name with
make mb source=<your_bucket1> dest=<your_bucket2>
```
2. Generate files with different sizes to source bucket(optional if you already have S3 files)
```
#we will generate 1mb 1.5mb 2mb files for testing
make s3files
```
3. Upload test files with different sizes to source bucket via aws cli (optional if you already have S3 files)
```
make upload 
#by default it will upload to bucket 'kvsource', can also set your bucket name with:
make upload  source=<your_bucket>
```
4. Build Docker Image
   ```sh
   make build 
   ```

## Usage
### Run  apllication locally
1. Before running the docker container, you can also run python application locally
```
copys3.py <sourcebucket> <destinationbucket> <threshold>
# in my AWS test account, example as
python3 copys3.py kvsource kvdest 3
```
2. Verify to see files were copied to kvdest bucket:
```sh
 aws s3 ls s3://kvdest
```

### Run the docker application

1. Run the application:
- use the 1.5MB as default threshold,copy files from 'kvsource' to 'kvdest'
```sh
  make run
```
- customize the bucket and size, for example, use the 1MB as size threshold,copy files from 'frombucket' to 'tobucket'
```sh
make run source=frombucket dest=tobucket size=1
```



<!-- ROADMAP -->
### Troubleshooting
1. if docker application does not work as expected, check the docker logs via:
```
#docker logs awscli
 object 1.5m is larger than 1048576 bytes
 copying object 1.5m to bucket kvdest
 object 2m is larger than 1048576 bytes
 copying object 2m to bucket kvdest
```

2. You can also manually run the python code as step 1 in Usage Section
```
python3 copys3.py kvsource kvdest 3
```

