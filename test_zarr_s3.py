import dask.array as da
import os

os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_access_key"
os.environ["AWS_DEFAULT_REGION"] = "us-west-1"
os.environ["AWS_ENDPOINT_URL"] = "http://localhost:4566"


def write_zarr_to_s3(data, s3_uri, key='data.zarr'):

    data.to_zarr(s3_uri + '/' + key, storage_options={'anon': False})

def read_zarr_from_s3(s3_uri, key='data.zarr'):

    return da.from_zarr(s3_uri + '/' + key, storage_options={'anon': False})

if __name__ == "__main__":
    data_to_write = da.from_array([[1, 2], [3, 4]], chunks=(2, 2))
    s3_bucket_uri = 's3://archive-bucket'

    write_zarr_to_s3(data_to_write, s3_bucket_uri)

    data_read = read_zarr_from_s3(s3_bucket_uri)

    print("Data read from S3:")
    print(data_read.compute())
