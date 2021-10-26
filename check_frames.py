# %%  This cell can extract the timestamps of frames in a video
from typing import List, Dict
# file = r"/media/storage01/TBRData/Box2/Data/Assessment_Raw_Baseline/TBS0001BL0120200930/TBS0001BL0120200930Kinect_PART2/OF_PWH_10F_202009301640_Far.mkv"
video_file = "/media/storage-ssd/peter/video/OF_PWH_10F_202009301640_Far.combined.mkv"
timestamp_file = "timestamps/OF_PWH_10F_202009301640_Far.combined.mkv.txt"

import cv2
def get_timestamp(file:str)->List:
    timestamps = []
    cap = cv2.VideoCapture(file)
    timestamp_pre = 0
    while(cap.isOpened()):
        frame_exists, curr_frame = cap.read()
        if frame_exists:
            timestamp_cur = cap.get(cv2.CAP_PROP_POS_MSEC)
            timestamps.append(timestamp_cur)
            
            # print(timestamp_cur - timestamp_pre)
            # timestamp_pre = timestamp_cur
        else:
            break
    cap.release()
    return timestamps

timestamps = get_timestamp(video_file)
print(f"#frames: {len(timestamps)}")
with open(timestamp_file, "w") as f:
    for ts in timestamps:
        f.write(f"{ts:.5f}\n")

# %% This cell can draw delta of timestamps
#  which could be used for checking intervals between timeframes

import plotly.express as px
import pandas as pd
from typing import List, Dict


files = ["timestamps/OF_PWH_10F_202009301640_Far.mjpeg.mkv.txt"]
def draw(timestamps: Dict[str, List]):
    df = pd.DataFrame.from_dict(timestamps, orient='index')
    df = df.transpose()
    #  ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html
    df_delta = df.diff()
    fig = px.line(df_delta)
    fig.show()


timestamps = {}
for f in files:
    with open(f, "r") as _f:
        lines = _f.readlines()
        data = [float(line.rstrip()) for line in lines]
        timestamps[f] = data
draw(timestamps)

    


# %% get the number of frames of a video
# THIS METHOD DOES NOT WORK
import cv2
video_file = "C:/Users/trist/Videos/Kinect/20210909140147/OF_PWH_8F_202109091401_Close.mkv"
cap = cv2.VideoCapture(video_file)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"#frames = {num_frames}")

# %% 
# refer to: https://stackoverflow.com/a/47743467
def update_fps(file:str, new_fps: float):
    # vidcap = cv2.VideoCapture('Wildlife.mp4') 
    # def getFrame(sec): 
    #     vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    #     hasFrames,image = vidcap.read() 
    #     if hasFrames: 
    #         cv2.imwrite("frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file 
    #     return hasFrames 
    # sec = 0 
    # frameRate = 0.5  # it will capture image in each 0.5 second 
    # success = getFrame(sec) 
    # while success: 
    #     sec = sec + frameRate 
    #     sec = round(sec, 2) 
    #     success = getFrame(sec) 
    pass
    # ffmpeg -r [fps] -i raw.mkv -c:v mjpeg output.mkv