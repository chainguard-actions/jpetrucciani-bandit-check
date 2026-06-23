import subprocess

# B602: subprocess call with shell=True is a security issue
subprocess.call("ls", shell=True)
