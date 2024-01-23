# localstack-aws-zarr

This an experimental repository, to tests zarr I/O on s3 object-storage via localstack.


## Setup

Deploy localstack using docker:
```bash
docker compose up -d
```

Install `awscli` and `awscli-local` (wrapper of `awscli`) in a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install awscli awscli-local
```

Create and list s3 buckets
```bash
source venv/bin/activate
awslocal s3 mb s3://archive-bucket/
awslocal s3 cp test.txt s3://archive-bucket/
awslocal s3 ls s3://archive-bucket/
# 2024-01-09 15:29:10          5 test.txt
```

## Run simple test

Instal requirements (note that only `zarr` and `dask[array]` are needed at this point) and run basic example:
```console
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 example_zarr_s3.py
Remove group_url='s3://archive-bucket/my_group.zarr', if it exists
Opened root_group=<zarr.hierarchy.Group '/'>
Created subgroup=<zarr.hierarchy.Group '/subgroup'>
Write data to group_url='s3://archive-bucket/my_group.zarr'
Read data from array_0_url='s3://archive-bucket/my_group.zarr/array_0'
  actual_data=dask.array<from-zarr, shape=(4,), dtype=int64, chunksize=(2,), chunktype=numpy.ndarray>
  actual_data.compute()=array([0, 0, 0, 0])
Write data to array_1_url='s3://archive-bucket/my_group.zarr/subgroup/array_1'
Read data from array_1_url='s3://archive-bucket/my_group.zarr/subgroup/array_1'
  actual_data=dask.array<from-zarr, shape=(4,), dtype=int64, chunksize=(2,), chunktype=numpy.ndarray>
  actual_data.compute()=array([1, 1, 1, 1])
```

or
```console
$ source venv/bin/activate
$ python example_zarr_s3_access_parent_group.py
Remove group_url='s3://archive-bucket/my_other_group.zarr', if it exists
Opened root_group=<zarr.hierarchy.Group '/'>, with root_group.attrs.asdict()={'level': 0}
Opened B_subgroup=<zarr.hierarchy.Group '/B'>, with B_subgroup.attrs.asdict()={'level': 1}
Opened B_03_subgroup=<zarr.hierarchy.Group '/B/03'>, with B_03_subgroup.attrs.asdict()={'level': 2}
Opened B_03_0_subgroup=<zarr.hierarchy.Group '/B/03/0'>, with B_03_0_subgroup.attrs.asdict()={'level': 3}
B_03_0_subgroup_url='s3://archive-bucket/my_other_group.zarr/B/03/0'
parent_url='s3://archive-bucket/my_other_group.zarr/B/03'
--------------------------------------------------------------------------------

Opened root_group=<zarr.hierarchy.Group '/'>, with root_group.attrs.asdict()={'level': 0}
Opened C_subgroup=<zarr.hierarchy.Group '/'>, with C_subgroup.attrs.asdict()={'level': 1}
Opened C_03_subgroup=<zarr.hierarchy.Group '/03'>, with C_03_subgroup.attrs.asdict()={'level': 2}
Opened C_03_0_subgroup=<zarr.hierarchy.Group '/03/0'>, with C_03_0_subgroup.attrs.asdict()={'level': 3}
wrong_C_03_0_subgroup_url='s3://archive-bucket/my_other_group.zarr/03/0'
parent_url='s3://archive-bucket/my_other_group.zarr/C/03'
--------------------------------------------------------------------------------
```


## Out-of-date: Run a simple test for zarr

> WARNING: This section and the corresponding scripts must be reviewed.

The `test_zarr_from_local_fs.py` script makes three steps:
1. creates an HCS zarr file 
2. push the zarr to an s3 bucket
3. read a zarr slice from the s3 bucket
(The script is mostly like this one [link](https://forum.image.sc/t/should-it-be-possible-to-load-an-ome-zarr-hcs-plate-directly-from-s3/86956))

```bash
source venv/bin/activate
pip install -r requirements.txt
python test_omezarr_from_local_fs.py
```

The `test_omezarr_s3.py` script creates the zarr file in an s3 bucket and then read a slice. 

The `test_zarr_s3.py` simply create a zarr file from a dask array on a s3 bucket. 

### Spoiler alert

Writing a file on localfs seems to be faster than creating the zarr on s3 bucket. Creating it locally shows an elapsed time ~100 times faster than creating it on s3

Elapsed time for writing on localfs:  0.03611588500007201 sec

Elapsed time for writing on s3:  3.326315969999996 sec
