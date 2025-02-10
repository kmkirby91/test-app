import subprocess
import os

# Define the working directory where `newapp.py` is located
workdir = "/config/workspace/github/test-app"  # Update if needed
script_name = "newapp.py"

# Check if the script exists
script_path = os.path.join(workdir, script_name)
if not os.path.exists(script_path):
    print(f"🚨 Error: '{script_path}' not found! Check your paths.")
    exit(1)

# Miniconda activation path
conda_sh_path = "/config/miniconda3/etc/profile.d/conda.sh"

# Build the command to ensure we run it from the correct directory
commands = [
    f"cd {workdir}",  # Go to the correct directory
    f"source {conda_sh_path}",  # Load Miniconda (adjust path if needed)
    "conda activate kkpop",  # Activate your environment
    f"streamlit run {script_name} --server.port 7777"  # Run Streamlit
]

# Join and execute the commands
bash_command = " && ".join(commands)
subprocess.run(bash_command, shell=True, executable="/bin/bash")
