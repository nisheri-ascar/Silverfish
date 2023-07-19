import logging
import sys
import subprocess
import json

# Set default logging level to INFO
logging.basicConfig(level="INFO", format="[%(asctime)s - %(levelname)s - %(threadName)s] %(message)s", force=True)

# Check if current python version is 3.8
if sys.version_info < (3, 8):
    logging.fatal('McPy needs Python version 3.8.0 or higher to run! Current version is %s.%s.%s' % (
        sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
    sys.exit(-4)

# Make sure pip is installed
logging.info("Making sure pip is installed...")
# Instead of previous debian specific solution, tell user instead to install it. 
try:
    subprocess.check_call([sys.executable, '-m' 'pip' '-V'])
except subprocess.CalledProcessError:
    logging.fatal("pip is not installed. You can find resources online on how to install it specifically for your operating system.")
    sys.exit(-4)
logging.info("Pip is present")


# Make sure that dependencies are installed
logging.info("Installing dependencies...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
try:
    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['git', 'submodule', 'init'])
    subprocess.check_call(['git', 'submodule', 'update'])
    logging.info("Dependencies installed")
except subprocess.CalledProcessError:
    logging.fatal("Git is not installed! Please install it!")

# Finishing up
with open('releases.json', 'r') as f:
    release_info = json.load(f)

for releases in release_info:
    version = releases["mcpyVersion"]

logging.info("McPy version " + version + " is ready. You can run the server with python3 main.py")
