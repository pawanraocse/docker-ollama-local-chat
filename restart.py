import subprocess
import time

from config import MODEL_NAME, OLLAMA_CONTAINER

def run_cmd(command, check=True):
    result = subprocess.run(command, shell=True)
    if check and result.returncode != 0:
        print(f"Command failed: {command}")
        exit(result.returncode)

def main():
    print("Stopping and removing existing containers...")
    run_cmd("docker-compose stop")

    print("Building containers...")
    run_cmd("docker-compose build")

    print("Starting Ollama container...")
    run_cmd(f"docker-compose up -d {OLLAMA_CONTAINER}")

    print(f"Waiting for {OLLAMA_CONTAINER} to be ready...")
    time.sleep(5)  # Give it a few seconds to fully start

    print(f"Pulling model: {MODEL_NAME}")
    run_cmd(f"docker exec {OLLAMA_CONTAINER} ollama pull {MODEL_NAME}")

    print("Running Python app (interactive)...")
    run_cmd("docker-compose run --rm python-app")

if __name__ == "__main__":
    main()
