import os


# path = r"/media/storage-ssd/AdminData/TRS Zoom/"
# list_subfolders_with_paths = [f.name for f in os.scandir(path) if f.is_dir()]
# area_learder_recordings = []
# for item in list_subfolders_with_paths:
#     if "leader" in item.lower():
#         area_learder_recordings.append(item)
# print(len(area_learder_recordings))
# for i in area_learder_recordings:
#     print(i)

# %% given #frames and fps, calculate the duration
import datetime
num_frames = 162965
fps = 30
print(datetime.timedelta(seconds=num_frames/fps))

# %% given a timestamp, calculate the duration
import datetime
ts_ms = 5414777.00000
print(datetime.timedelta(milliseconds=ts_ms))

# %% given num_frames and duration, calculate the fps
import datetime
num_frames = 162115
duration = datetime.timedelta(hours=1, minutes=30, seconds=5.97)
print(f"fps: {num_frames/duration.total_seconds()}/s")
