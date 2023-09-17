import subprocess
import sys

def create_virtualenv(venv_name):
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to create virtual environment.")
        exit(1)

def install_dependencies(venv_name):
    try:
        subprocess.run([venv_name + "\\Scripts\\pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to install dependencies.")
        exit(1)

if __name__ == "__main__":
    venv_name = "my_project_venv"

    # Step 1: Create a virtual environment
    print(f"Step 1: Creating a virtual environment ({venv_name})")
    create_virtualenv(venv_name)

    # Step 2: Activate the virtual environment (Windows)
    print("Step 2: Activating the virtual environment (Windows)")
    activate_script = venv_name + "\\Scripts\\activate.bat"
    subprocess.run([activate_script], shell=True, check=True)

    # Step 3: Install dependencies from requirements.txt
    print("Step 3: Installing project dependencies from requirements.txt")
    install_dependencies(venv_name)

    # Step 4: Deactivate the virtual environment (Windows)
    print("Step 4: Deactivating the virtual environment (Windows)")
    subprocess.run(["deactivate"], shell=True, check=True)

    print("Project setup completed successfully.")
