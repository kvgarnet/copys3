# copys3


#docker run  -dti -v ~/.aws:/root/.aws  --name awscli myimage
will use the 3MB as default threshold,copy bucket from 'kvsource' to 'kvdest'
#docker run  -dti -v ~/.aws:/root/.aws  --name awscli myimage  kvsource kvdest 1
will use the 1MB as size threshold,copy bucket from 'kvsource' to 'kvdest'
# docker logs awscli
object 1.5m is larger than 1048576 bytes
copying object 1.5m to bucket kvdest
object 2m is larger than 1048576 bytes
copying object 2m to bucket kvdest
object 3m is larger than 1048576 bytes
copying object 3m to bucket kvdest
object 4m is larger than 1048576 bytes
copying object 4m to bucket kvdest

verify kvdest bucket that file were copied successfully
# aws s3 ls s3://kvdest   
2021-02-20 22:24:17    1536000 1.5m
2021-02-20 22:24:17    2097152 2m
2021-02-20 22:24:17    3145728 3m
2021-02-20 22:24:17    4194304 4m

verify kvsource bucket's file that file size less than 1M were not copied
# aws s3 ls s3://kvsource         
2021-02-20 22:06:05    1536000 1.5m
2021-02-20 22:05:58    1048576 1m
2021-02-20 21:03:39      29696 29k
2021-02-20 21:13:38    2097152 2m
2021-02-20 21:03:45      30720 30k
2021-02-20 21:04:14      31744 31k
2021-02-20 21:13:45    3145728 3m
2021-02-20 21:14:40    4194304 4m
2021-02-20 14:10:27      67092 s3source
2021-02-20 14:31:50         87 shift.sh
