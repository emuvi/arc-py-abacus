import os
import subprocess

def backup():
    doing = []
    for _, dirs, _ in os.walk("D:\\Abacus"):
        for folder in dirs:
            command = "rclone -v sync D:\\Abacus\\" + folder + " server:/mnt/HDS1/Abacus/" + folder
            doing.append(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE))
        break
    return doing
