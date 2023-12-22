import zarr
import string
import numpy as np
from ome_zarr.writer import write_image, write_plate_metadata, write_well_metadata
import s3fs
import os
import napari

os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key_id'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_access_key'
os.environ['AWS_DEFAULT_REGION'] = 'us-west-1'
os.environ['AWS_ENDPOINT_URL'] = 'http://localhost:4566'



# write file to local
def write_HCS_plate_on_s3(
    file_path, 
    well_paths = ["A/2", "B/3"], 
    num_rows=2, 
    num_cols=3, 
    field_paths = ["0", "1", "2"],
    ):
    fs = s3fs.S3FileSystem(anon=True,
                           client_kwargs=dict(region_name='us-west-1')) # anon -> anonymous
    store = s3fs.S3Map(root=file_path, s3=fs)
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
            write_image(np.full((1, 1, 1, 256, 256), 10), image)
    print(f"Created: \n{root.get('A/2/0/0')[:]}\n")
    

s3_path = "s3://test-bucket/test.ome.zarr"

write_HCS_plate_on_s3(s3_path)


# read zarr

import zarr
fs = s3fs.S3FileSystem(anon=True,
                       client_kwargs=dict(region_name='us-west-1'))
store = s3fs.S3Map(root=s3_path, s3=fs)
root = zarr.group(store=store)

### if LRU, the second access is fastest
# cache = zarr.LRUStoreCache(store, max_size=2**28)
# root = zarr.group(store=cache)

print(f"Read: \n {root.get('A/2/0/0')[:]}\n")


# read file from s3 not working
# viewer = napari.Viewer()
# viewer.open(s3_path, plugin="napari-ome-zarr")