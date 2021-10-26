# Speeding up/slowing down video
# This method is lossless and apart from changing the timestamps, copies the video stream as-is. Use this if you require no other changes to your input video.
# ref: https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video

# 1. copy the video to a raw bitstream format.
# use 'mjpeg2jpeg' for source of the mjpeg format
ffmpeg -i /path/to/source/video.mkv -map 0:v -c:v copy -bsf:v mjpeg2jpeg /path/to/dest/video.mjpeg

# 2. generate new timestamps while muxing to a container.
# Will give a fps of 25, constantly
ffmpeg -fflags +genpts -r 25 -i /path/to/source/video.mjpeg -c:v copy /path/to/dest/video.mkv

# Note: for mjpeg, option '-f' is alaways needed, like below command.
# add -f mjpeg for the input stream for a specific fps
# ref: https://stackoverflow.com/questions/29058590/ffmpeg-starts-too-slow-when-using-ip-camera-the-same-as-using-opencv#comment46358286_29059267
ffmpeg -fflags +genpts -r 25 -f mjpeg -i /path/to/source/video.mjpeg -c:v copy /path/to/dest/video.mkv

# combine audio and video to form a single file
ffmpeg -i xx.mkv -i xx.wav -map 0:v -c:v copy -map 1:a -c:a copy out.mkv