import subprocess
import os


# B602: subprocess call with shell=True
def run_command(cmd):
    subprocess.call(cmd, shell=True)


# B605: start process with a shell
def execute(cmd):
    os.system(cmd)
