import os
import subprocess

def backup():
    doing = []
    for _, dirs, _ in os.walk("D:\\Abacus"):
        for folder in dirs:
            command = "rclone -v sync D:\\Abacus\\" + folder + " cloud:/Abacus/" + folder
            if (folder == "DropBox"):
                command = "rclone -v sync cloud:/Abacus/" + folder + " D:\\Abacus\\" + folder
            doing.append(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE))
        break
    return doing
