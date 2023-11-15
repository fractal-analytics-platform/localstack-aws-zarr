# localstack-aws-zarr
Tests with localstack, aws and zarr I/O


```
$ python3 -m venv venv
$ source venv/bin/activate

$ python3 -m pip install --upgrade localstack
$ python3 -m pip install awscli awscli-local
```

```
$ git clone https://github.com/localstack/localstack-demo.git
$ cd localstack-demo
$ make deploy
```

```
$ awslocal s3 ls s3://archive-bucket/
                           PRE a2b95efc/
2023-11-15 11:40:28     202151 architecture.png
2023-11-15 11:40:28       6514 index.html
```
