import os
import subprocess

def restore():
    doing = []
    for _, dirs, _ in os.walk("/mnt/hda/Abacus"):
        for folder in dirs:
            command = "rclone -v sync \"server:/mnt/HD01/Abacus/" + folder + "\" \"/mnt/hda/Abacus/" + folder + "\""
            doing.append(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE))
        break
    return doing

if (__name__ == '__main__'):
    doing = []
    doing.extend(restore())
    for process in doing:
        process.wait()
