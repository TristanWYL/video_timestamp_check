# Speeding up/slowing down video
# ref: https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video
ffmpeg -i /media/storage01/TBRData/Box2/Data/Assessment_Raw_Baseline/TBS0001BL0120200930/TBS0001BL0120200930Kinect_PART2/OF_PWH_10F_202009301640_Far.mkv -map 0:v -c:v copy -bsf:v mjpeg2jpeg /media/storage-ssd/peter/video/OF_PWH_10F_202009301640_Far.mjpeg
# Will give a fps of 25, constantly
ffmpeg -fflags +genpts -r 20 -i /media/storage-ssd/peter/video/OF_PWH_10F_202009301640_Far.mjpeg -c:v copy /media/storage-ssd/peter/video/OF_PWH_10F_202009301640_Far.mkv
# add -f mjpeg for the input stream for a specific fps
# ref: https://stackoverflow.com/questions/29058590/ffmpeg-starts-too-slow-when-using-ip-camera-the-same-as-using-opencv#comment46358286_29059267
ffmpeg -fflags +genpts -r 20 -f mjpeg -i /media/storage-ssd/peter/video/OF_PWH_10F_202009301640_Far.mjpeg -c:v copy /media/storage-ssd/peter/video/OF_PWH_10F_202009301640_Far.mkv

# combine audio and video
ffmpeg -i xx.mkv -i xx.wav -map 0:v -c:v copy -map 1:a -c:a copy out.mkv