import zarr
import dask.array as da
import os
import subprocess
import shlex
from devtools import debug

os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_access_key"
os.environ["AWS_DEFAULT_REGION"] = "us-west-1"
os.environ["AWS_ENDPOINT_URL"] = "http://localhost:4566"


# Define URL of root group
group_url = "/tmp/rootgroup.zarr"
group_url = "s3://archive-bucket/my_other_group.zarr"

# Remove Zarr group
print(f"Remove {group_url=}, if it exists")
subprocess.run(
    shlex.split(f"awslocal s3 rm {group_url} --recursive"),
    # shlex.split(f"rm {group_url} --recursive"),
    check=True,
    capture_output=True,
)

# Example 1 (strict assumptions about group creation)

# Create group and subgroups
root_group = zarr.open_group(group_url)
root_group.attrs.put({"level": 0})
print(f"Opened {root_group=}, with {root_group.attrs.asdict()=}")
B_subgroup = root_group.create_group("B")
B_subgroup.attrs.put({"level": 1})
print(f"Opened {B_subgroup=}, with {B_subgroup.attrs.asdict()=}")
B_03_subgroup = B_subgroup.create_group("03")
B_03_subgroup.attrs.put({"level": 2})
print(f"Opened {B_03_subgroup=}, with {B_03_subgroup.attrs.asdict()=}")
B_03_0_subgroup = B_03_subgroup.create_group("0")
B_03_0_subgroup.attrs.put({"level": 3})
print(f"Opened {B_03_0_subgroup=}, with {B_03_0_subgroup.attrs.asdict()=}")
print("-" * 80)

# Extract parent group of subgroup
B_03_0_subgroup_url = f"{group_url}/{B_03_0_subgroup.path}"
print(f"{B_03_0_subgroup_url=}")
parent_url = "/".join(B_03_0_subgroup_url.split("/")[:-1])
print(f"{parent_url=}")
parent_group = zarr.open_group(parent_url)
assert parent_group.attrs["level"] == 2, "Wrong group was loaded"
print("All good")
print("-" * 80 + "\n")


# Example 2 (more loose assumptions about group creation)

# Create group and subgroups
root_group = zarr.open_group(group_url)
root_group.attrs.put({"level": 0})
print(f"Opened {root_group=}, with {root_group.attrs.asdict()=}")
_C_subgroup = root_group.create_group("C")
C_subgroup = zarr.open_group(f"{group_url}/C")
C_subgroup.attrs.put({"level": 1})
print(f"Opened {C_subgroup=}, with {C_subgroup.attrs.asdict()=}")
C_03_subgroup = C_subgroup.create_group("03")
C_03_subgroup.attrs.put({"level": 2})
print(f"Opened {C_03_subgroup=}, with {C_03_subgroup.attrs.asdict()=}")
C_03_0_subgroup = C_03_subgroup.create_group("0")
C_03_0_subgroup.attrs.put({"level": 3})
print(f"Opened {C_03_0_subgroup=}, with {C_03_0_subgroup.attrs.asdict()=}")
print("-" * 80)

# Extract parent group of subgroup
wrong_C_03_0_subgroup_url =f"{group_url}/{C_03_0_subgroup.path}"
print(f"{wrong_C_03_0_subgroup_url=}")
C_03_0_subgroup_url = f"{group_url}/C/03/0"
parent_url = "/".join(C_03_0_subgroup_url.split("/")[:-1])
print(f"{parent_url=}")
parent_group = zarr.open_group(parent_url)
assert parent_group.attrs["level"] == 2, "Wrong group was loaded"
print("All good")
print("-" * 80 + "\n")
