from multiprocessing import Process

def run_script1():
    import subprocess
    subprocess.run(['python', '/Users/jonty/Desktop/Docs/To Sift/HEMP SHAKES/HEMP WEBSITE/backend_server_03.py'])

def run_script2():
    import subprocess
    subprocess.run(['python', '/Users/jonty/Desktop/Docs/To Sift/HEMP SHAKES/HEMP WEBSITE/virtual_server_01.py'])

if __name__ == '__main__':
    p1 = Process(target=run_script1)
    p2 = Process(target=run_script2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
