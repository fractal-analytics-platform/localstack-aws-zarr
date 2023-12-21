# localstack-aws-zarr
Tests with localstack, aws and zarr I/O

Deploy localastack using docker:

```bash
docker compose up -d
```


Install awscli and awscli-local (wrapper of awscli)

```bash
python3 -m venv venv
source venv/bin/activate

python3 -m pip install awscli awscli-local

```

Create and list s3 buckets

```bash
source venv/bin/activate
awslocal s3 mb s3://archive-bucket/

awslocal s3 ls s3://archive-bucket/
#                            PRE a2b95efc/
# 2023-11-15 11:40:28     202151 architecture.png
# 2023-11-15 11:40:28       6514 index.html
```


## Run a simple test for zarr

The `test_zarr.py` script makes three steps:
1. creates an HCS zarr file 
2. push the zarr to an s3 bucket
3. read a zarr slice from the s3 bucket
(The script is mostly like this one [link](https://forum.image.sc/t/should-it-be-possible-to-load-an-ome-zarr-hcs-plate-directly-from-s3/86956))

```bash
source venv/bin/activate
pip install -r requirements.txt
python test_zarr.py
```