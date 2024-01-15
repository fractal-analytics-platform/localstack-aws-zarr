import sys
import zarr
import dask.array as da
import os
import subprocess
import shlex

os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_access_key"
os.environ["AWS_DEFAULT_REGION"] = "us-west-1"
os.environ["AWS_ENDPOINT_URL"] = "http://localhost:4566"


# Define URL of root group
group_url = f"s3://archive-bucket/my_group.zarr"

# Create group and subgroup
print("Open group")
root_group = zarr.open_group(group_url)
print(f"{root_group=}")
print()
print("Create subgroup")
subgroup = root_group.create_group("subgroup")
print(f"{subgroup=}")
print()

# Write data to array in root group
array_0_url = f"{group_url}/array_0"
print(f"Write data to {group_url=}")
data_0 = da.from_array([0, 0, 0, 0], chunks=(2,))
data_0.to_zarr(array_0_url, storage_options={'anon': False})
print()

# Read array-0 data
print(f"Read data from {array_0_url=}")
actual_data = da.from_zarr(array_0_url, storage_options={'anon': False})
print(f"{actual_data=}")
print(f"{actual_data.compute()=}")
print()

# Write data to array in subgroup
subgroup_url = f"{group_url}/subgroup"
array_1_url = f"{subgroup_url}/array_1"
print(f"Write data to {array_1_url=}")
data_1 = da.from_array([1, 1, 1, 1], chunks=(2,))
data_1.to_zarr(array_1_url, storage_options={'anon': False})
print()

# Read array-0 data
print(f"Read data from {array_1_url=}")
actual_data = da.from_zarr(array_1_url, storage_options={'anon': False})
print(f"{actual_data=}")
print(f"{actual_data.compute()=}")
print()

# Clean up
print("Now remove the s3 object")
subprocess.run(
    shlex.split(
        f"awslocal s3 rm {group_url} --recursive"
    ),
    check=True,
)
