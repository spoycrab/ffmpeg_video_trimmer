import os, fnmatch, subprocess

def tipoVid(vid):
    fileType = os.path.splitext(vid)[1]
    
    start = input(f'{vid}\nStart(00:00:00)\n>> ')
    end = input(f'\nEnd(00:00:00)\n>> ')
    if start == "":
        start == "00:00:00"

    if end == "":
        end = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', vid], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #Get video duration
        end = float(end.stdout)

    os.system(f'ffmpeg -i "{vid}" -ss {start} -to {end} cut{fileType}')

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.mp4') or fnmatch.fnmatch(file, '*.webm') or fnmatch.fnmatch(file, '*.mov') or fnmatch.fnmatch(file, '*.mkv'):
        tipoVid(file)
        break

input("Done")