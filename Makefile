#vars
source ?= kvsource
dest ?= kvdest
size ?= 1.5
#Dockerfile var
py_ver=3.6
.PHONY: help mb s3files upload build run all
help:
	@echo 'Usage: make [TARGET] [ARGUMENTS]'
	@echo ""
	@echo "Makefile arguments:"
	@echo ""
	@echo "source  - source bucket name"
	@echo "dest    - destination bucket name"
	@echo "size    - threshold size in MB"
	@echo "py_ver  - Python image Version"
	@echo ""
	@echo "Makefile Targets:"
	@echo ""
	@echo "mb      - create S3 buckets"
	@echo "s3files - create S3 testfiles"
	@echo "upload  - upload S3 testfiles to sourcebucket"
	@echo "build   - build docker image"
	@echo "run     - run docker app"
	@echo "all     - run above targets in one shot"
all: mb s3files upload build run
mb: sourcebucket destbucket
	echo "buckets created"
sourcebucket:
	aws s3 mb s3://$(source)
	touch sourcebucket
destbucket:
	aws s3 mb s3://$(dest)
	touch destbucket
s3files: 1m 1.6m 2m
	echo "S3 files created"
1m:
	dd if=/dev/zero of=./1m bs=1k count=1024
1.6m:
	dd if=/dev/zero of=./1.6m bs=1k count=1600
2m:
	dd if=/dev/zero of=./2m bs=1M count=2
upload:
	for file in ./*m; do  aws s3 cp $$file s3://$(source) ; done
build:
	docker build  --build-arg PYTHON_VER=${py_ver} -t myimage .
run:
	docker run  -dti -v ~/.aws:/root/.aws  --name awscli myimage $(source) $(dest) $(size)
clean:
	docker rm -f awscli >/dev/null 2>&1 && echo "Container app deleted."
	docker rmi myimage >/dev/null 2>&1 || echo "image deleted"
	rm -f 1m 1.6m 2m sourcebucket destbucket&& echo "all file cleaned" 
	aws s3 rb --force s3://$(source)
	aws s3 rb --force s3://$(dest)
	echo "S3 buckets removed"
