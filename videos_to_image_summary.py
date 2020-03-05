import glob, os
import subprocess
import shutil
import argparse

## interface
parser = argparse.ArgumentParser(description='simple .mp4 videos to summary thumbnail image converter')
parser.add_argument('-v','--video_path', type=str, dest='video_path', action='store', default="/mnt/student/EmCaR/2_data/360p/videos",
                    help='specify the path to the videos')
parser.add_argument('-i', '--image_path', type=str, dest='model_type', action='store', default="/mnt/student/EmCaR/2_data/360p/videos/frames", 
                    help='specify the path where the extracted images should be stored (WARNNING: overwritten if exists)')
parser.add_argument('-t','--timestamp', type=str, dest='timestamp', action='store', default='00:01:00.000', 
                    help='specify the timestamp where the snapshot should be take from the videos in hh:mm:ss:ms e.g. 00:01:00.000')
parser.add_argument('--title', type=str, dest='title', action='store', default='MuSe-CAR', 
                    help='specify outputfile name and header')

args = parser.parse_args()

print('Change to video path: ' + video_input_path)
os.chdir(args.video_path)

if not os.path.exists(args.image_path):
    os.makedirs(args.image_path)
else:
    shutil.rmtree(args.image_path)           # Removes all the subdirectories!
    os.makedirs(args.image_path)

for video_input_path in glob.glob("*.mp4"):

    img_output_path = args.image_path + os.path.sep + 'capture-'+ video_input_path.split('.')[-2] + '.png'
    print('Create thumbnail: ' + img_output_path)
    subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', args.timestamp, '-vf','scale=-1:120','-vcodec','png','-vframes', '1', img_output_path])

print("Frame extraction completed")

os.chdir(args.image_path)
subprocess.call(['montage','-title',args.title,'-geometry','+4+4','capture*.png',args.title+'_output.png'])
