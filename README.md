# localstack-aws-zarr
Tests with localstack, aws and zarr I/O


```
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade localstack
python3 -m pip install awscli awscli-local

localstack --version
# 3.0.0

aws --version
# aws-cli/1.30.4 Python/3.10.12 Linux/6.2.0-36-generic botocore/1.32.4
```

```
source venv/bin/activate

localstack start

localstack start

     __                     _______ __             __
    / /   ____  _________ _/ / ___// /_____ ______/ /__
   / /   / __ \/ ___/ __ `/ /\__ \/ __/ __ `/ ___/ //_/
  / /___/ /_/ / /__/ /_/ / /___/ / /_/ /_/ / /__/ ,<
 /_____/\____/\___/\__,_/_//____/\__/\__,_/\___/_/|_|

 💻 LocalStack CLI 3.0.0

[13:59:59] starting LocalStack in Docker mode 🐳                                                                                                                                                   localstack.py:495
────────────────────────────────────────────────────────────────────────────────── LocalStack Runtime Log (press CTRL-C to quit) ───────────────────────────────────────────────────────────────────────────────────

LocalStack version: 2.3.3.dev
LocalStack Docker container id: 8d7420ab8a95
LocalStack build date: 2023-11-15
LocalStack build git hash: 10940eb0

2023-11-21T13:00:02.474  INFO --- [-functhread6] hypercorn.error            : Running on https://0.0.0.0:4566 (CTRL + C to quit)
2023-11-21T13:00:02.474  INFO --- [-functhread6] hypercorn.error            : Running on https://0.0.0.0:4566 (CTRL + C to quit)
2023-11-21T13:00:02.562  INFO --- [  MainThread] localstack.utils.bootstrap : Execution of "start_runtime_components" took 602.12ms
Ready.
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
git clone https://github.com/localstack/localstack-demo.git
cd localstack-demo
make deploy
```


```
source venv/bin/activate
localstack stop
```
