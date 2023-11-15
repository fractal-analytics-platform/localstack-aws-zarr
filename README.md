# localstack-aws-zarr
Tests with localstack, aws and zarr I/O


```
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade localstack
python3 -m pip install awscli awscli-local

localstack --version
# 2.3.2

aws --version
# aws-cli/1.30.0 Python/3.10.12 Linux/6.2.0-36-generic botocore/1.32.0

```

```
source venv/bin/activate
git clone https://github.com/localstack/localstack-demo.git
cd localstack-demo
make deploy
```

```
source venv/bin/activate

localstack start
# ...
#  💻 LocalStack CLI 2.3.2
# 
# [11:54:57] starting LocalStack in Docker mode 🐳                                                                                                                                                   localstack.py:495
# 2023-11-15T11:54:57.786  WARN --- [  MainThread] l.utils.docker_utils       : Unexpected error when attempting to determine container port status: ('Docker process returned with errorcode 125', b'', b'docker: Error response from daemon: driver failed programming external connectivity on endpoint laughing_napier (7ef2c92d4a58e8b451569d7d7de20e83f51613ddbc718df176065bb9824fae2e): Error starting userland proxy: listen tcp4 0.0.0.0:53: bind: address already in use.\n')
# ────────────────────────────────────────────────────────────────────────────────── LocalStack Runtime Log (press CTRL-C to quit) ───────────────────────────────────────────────────────────────────────────────────
# 
# LocalStack version: 2.3.3.dev
# LocalStack Docker container id: cc3245c3e34b
# LocalStack build date: 2023-11-15
# LocalStack build git hash: 10940eb0
# 
# 2023-11-15T10:54:59.988  INFO --- [-functhread6] hypercorn.error            : Running on https://0.0.0.0:4566 (CTRL + C to quit)
# 2023-11-15T10:54:59.988  INFO --- [-functhread6] hypercorn.error            : Running on https://0.0.0.0:4566 (CTRL + C to quit)
# Ready.
```

```
source venv/bin/activate
awslocal s3 ls s3://archive-bucket/
#                            PRE a2b95efc/
# 2023-11-15 11:40:28     202151 architecture.png
# 2023-11-15 11:40:28       6514 index.html
```

```
source venv/bin/activate
localstack stop
```
