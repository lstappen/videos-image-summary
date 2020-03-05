# videos-image-summary
Lightweight script to extract thumbnails (frames) from multiple videos at a specified time (timestamp) and join them into one overview image.

#### for example:
  ```
   python videos_to_image_summary.py -v './videos' -i './snapshots' --title 'Test'
```

 ![GitHub Logo](/output_compressed.jpeg)
### requirements (standard under Ubuntu and Python 3)
* System: ffmpeg, montage
* Python: subprocess, shutil, argparse, glob, os

### argparser arguments
 ```
usage: videos_to_image_summary.py [-h] [-v VIDEO_PATH] [-i MODEL_TYPE]
                                  [-t TIMESTAMP] [--title TITLE]

simple .mp4 videos to summary thumbmail image converter

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO_PATH, --video_path VIDEO_PATH
                        specify the path to the videos
  -i MODEL_TYPE, --image_path MODEL_TYPE
                        specify the path where the extracted images should be
                        stored (WARNNING: overwritten if exists)
  -t TIMESTAMP, --timestamp TIMESTAMP
                        specify the timestamp where the snapshot should be
                        take from the videos in hh:mm:ss:ms e.g. 00:01:00.000
  --title TITLE         specify outputfile name and header
 ```

