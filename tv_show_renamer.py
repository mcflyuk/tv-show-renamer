#
#	Martyn's TV show renaming script
#   Takes any filename and renames it using a 1x01, 1x02 naming format
#   Usage:
#       python tv_show_renamer.py <directory_containing_video_files>
#

import glob, sys, os

# Check whether a directory name has been passed
if len(sys.argv) < 2:
	sys.exit(0)

# Remember the original directory to return to
original_directory = os.getcwd()

# Change directory to the one given as an argument
os.chdir(sys.argv[1])

print 'Files re-named:'

# Read in the files
for video_files in glob.glob('*'):
    # Check the filename, if the first character isn't a number then don't do anything
    if video_files[0].isdigit():
        # Check if it's already in the 1x01 format
        if video_files[1] == 'x':
            # 2nd character is an 'x', add a zero to start with
            os.rename(video_files, '0' + video_files)
            print video_files + ' --> ' + '0' + video_files
            continue
        elif video_files[3] == 'x':
            os.rename(video_files, video_files[:2] + video_files[3:])
            print video_files + ' --> ' + video_files[:2] + video_files[3:]
            continue
        else:
            continue
        
        # Find the first space to give us the series and episode
        space = video_files.find(' ')

        episode_number = video_files[space - 2:space]
        series_number = video_files[0:space - 2]
        
        os.rename(video_files, series_number + 'x' + episode_number + video_files[space:])
        print video_files + ' --> ' + series_number + 'x' + episode_number + video_files[space:]
    else:
        # do nothing
        something = 1

# Return to the original directory
os.chdir(original_directory)

print 'TV show renaming complete!'