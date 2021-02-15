import LocalToServer

if (__name__ == '__main__'):
    doing = []
    doing.extend(LocalToServer.backup())
    for process in doing:
        process.wait()
