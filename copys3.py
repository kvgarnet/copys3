# -*- coding: utf-8 -*-
import argparse
import boto3
def getParser():
    desc='CLI tool to '
    usage=" python %(prog)s source_bucket dest_bucket size, use -h/--help or more help"
    #create a parser
    parser=argparse.ArgumentParser(description=desc, usage=usage)
    parser.add_argument('source',type=str, metavar="sourcebkt",help='name of source bucket')
    parser.add_argument('dest',type=str, metavar="destbkt",help='name of dest bucket')
    parser.add_argument('size',type=float, metavar="size",help='size of S3 object in unit mb')
    #parse the args
    args = parser.parse_args()
    return args

def copy_to_bucket(sourcebucket,destbucket,filename):
    copy_source = {
            'Bucket': sourcebucket,
            'Key': filename
        }
    obj=destbucket.Object(filename)
    obj.copy(copy_source)

def listobject(bucket):
    s3_resource = boto3.resource('s3')
    bucketname = s3_resource.Bucket(name=bucket)
    print(f"List objects in bucket {bucketname}:")
    objlst=[]
    for object in bucketname.objects.all():
        print(object.key)
        objlst.append(object.key)
    return objlst

def checkobject(sourcebucket,destbucket,sizemb):
    s3_resource = boto3.resource('s3')
    source_bucket = s3_resource.Bucket(name=sourcebucket)
    destbucket=s3_resource.Bucket(destbucket)
    for object in source_bucket.objects.all():
        if object.size > sizemb:
            # copyobj_lst.append(object.key)
            print(f"object {object.key} is larger than {sizemb} bytes")
            print(f"copying object {object.key} to bucket {destbucket.name}")
            copy_to_bucket(sourcebucket,destbucket,object.key)

def main():
    args=getParser()
    sourcebucket=args.source
    destbucket=args.dest
    #transform to mb from bytes
    sizemb=args.size*1024*1024
    checkobject(sourcebucket,destbucket,sizemb)

if __name__=='__main__':
    main()
