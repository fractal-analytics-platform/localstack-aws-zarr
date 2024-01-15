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
group_url = "s3://archive-bucket/my_group.zarr"

# Remove Zarr group
print(f"Remove {group_url=}, if it exists")
subprocess.run(
    shlex.split(f"awslocal s3 rm {group_url} --recursive"),
    check=True,
    capture_output=True,
)

# Create group and subgroup
root_group = zarr.open_group(group_url)
print(f"Opened {root_group=}")
subgroup = root_group.create_group("subgroup")
subgroup_url = f"{group_url}/subgroup"
print(f"Created {subgroup=}")

# Write data to array in root group
array_0_url = f"{group_url}/array_0"
print(f"Write data to {group_url=}")
data_0 = da.from_array([0, 0, 0, 0], chunks=(2,))
data_0.to_zarr(array_0_url, storage_options={'anon': False})

# Read array-0 data
print(f"Read data from {array_0_url=}")
actual_data = da.from_zarr(array_0_url, storage_options={'anon': False})
print(f"  {actual_data=}")
print(f"  {actual_data.compute()=}")

# Write data to array in subgroup
array_1_url = f"{subgroup_url}/array_1"
print(f"Write data to {array_1_url=}")
data_1 = da.from_array([1, 1, 1, 1], chunks=(2,))
data_1.to_zarr(array_1_url, storage_options={'anon': False})

# Read array-0 data
print(f"Read data from {array_1_url=}")
actual_data = da.from_zarr(array_1_url, storage_options={'anon': False})
print(f"  {actual_data=}")
print(f"  {actual_data.compute()=}")
