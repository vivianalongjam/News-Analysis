import subprocess, time

server = subprocess.Popen(["python", "-m", "flask", "run", "-h", "localhost", "-p"
    , "5000"])

while True:
    update = subprocess.Popen(["python", "update.py"])
    update.wait()
    update.kill()
    time.sleep(60)

