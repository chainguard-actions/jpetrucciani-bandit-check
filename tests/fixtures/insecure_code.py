# A Python file with known security issues for bandit to detect
import subprocess

def run_command(cmd):
    """Run a shell command - insecure use of shell=True."""
    return subprocess.call(cmd, shell=True)


def get_password():
    """Hardcoded password - security issue."""
    password = "supersecretpassword123"  # noqa
    return password
