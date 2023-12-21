import zarr
import string
from numpy import ones
import subprocess

from ome_zarr.io import parse_url
from ome_zarr.writer import write_image, write_plate_metadata, write_well_metadata
import s3fs
import os
# import napari

os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key_id'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_access_key'
os.environ['AWS_DEFAULT_REGION'] = 'us-west-1'
os.environ['AWS_ENDPOINT_URL'] = 'http://localhost:4566'


local_path = "test.ome.zarr"
s3_path = "s3://test-bucket/"


# write file to local
def write_HCS_plate(
    file_path, 
    well_paths = ["A/2", "B/3"], 
    num_rows=2, 
    num_cols=3, 
    field_paths = ["0", "1", "2"],
    ):
    store = parse_url(str(file_path), mode="w").store
    root = zarr.group(store=store)

    row_names = string.ascii_uppercase[: num_rows]
    col_names = list(map(str, range(1, num_cols + 1)))
    write_plate_metadata(root, row_names, col_names, well_paths)
    for wp in well_paths:
        row, col = wp.split("/")
        row_group = root.require_group(row)
        well = row_group.require_group(col)
        write_well_metadata(well, field_paths)
        for field in field_paths:
            image = well.require_group(str(field))
            write_image(ones((1, 1, 1, 256, 256)), image)

write_HCS_plate(local_path)



# copy file to s3
p = subprocess.Popen(f'awslocal s3 sync {local_path} {s3_path}', shell=True)
p.wait()


# read zarr
import zarr
fs = s3fs.S3FileSystem()
store = zarr.open(s3fs.S3Map(s3_path, s3=fs))
print(store.get("A/2/0/0")[:])


# read file from s3 not working
# viewer = napari.Viewer()
# viewer.open(s3_path, plugin="napari-ome-zarr")