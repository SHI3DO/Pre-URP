import subprocess


command = f"pip freeze > requirements.txt"
subprocess.run(command, shell=True)

