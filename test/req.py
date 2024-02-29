import subprocess
import sys


def install_dependencies(requirements_path='requirements.txt'):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])
        print("All dependencies have been installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing dependencies: {e}")


if __name__ == "__main__":
    install_dependencies()
