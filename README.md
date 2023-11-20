# Welcome to Git Commit Metrics!

Gather metrics from a commits within a GIT repository.

## Prequisites:
1. a version of python must be installed (see Python Installation Guide below)
2. Install GitPython: First, ensure that GitPython is installed in your Python environment:

*bash:*

    pip install GitPython

## Running the Script:
    
  1. Clone this repository, which in includes the Python file called `RetrieveCommitMetrics.py`.
  2. Run it in a Python environment where GitPython is installed.
  3. Follow the prompts to input the repository URL and local folder name.
  4. A directory call `repo-metrics` will be created in the same folder as the RetrevievCommitMetrics.py exists
  5. The requested repository will be cloned to the `repo-metrics` folder
  6. The output CSV file will be named the same as the {repository folder}.csv
  
The script will clone the repository, extract the commit metrics, and save them to a CSV file in the specified directory. Remember, you need to have Git installed on your machine for GitPython to work properly.


## Python Installation Guide

This guide provides step-by-step instructions on how to install Python on Windows and macOS.

#### For Windows:

1.  **Download Python**:
    
    -   Go to the official Python website: [python.org](https://www.python.org/)
    -   Navigate to the Downloads section and choose the latest version for Windows.
    -   Click on the download link for Windows Installer.
2.  **Run the Installer**:
    
    -   Once the installer is downloaded, run it.
    -   Make sure to check the box that says "Add Python 3.x to PATH" before clicking "Install Now".
3.  **Verify the Installation**:
    
    -   Open the Command Prompt.
    -   Type `python --version` and press Enter.
    -   If Python is successfully installed, you should see the version number.

#### For macOS:

1.  **Download Python**:
    
    -   Visit the official Python website: [python.org](https://www.python.org/)
    -   Go to the Downloads section and select the latest version for macOS.
    -   Click on the download link for macOS Installer.
2.  **Run the Installer**:
    
    -   Once downloaded, open the installer package.
    -   Follow the prompts in the Python Installer.
3.  **Verify the Installation**:
    
    -   Open the Terminal.
    -   Type `python3 --version` and press Enter.
    -   The version number should display if the installation was successful.

#### Notes:

-   **Windows**: Newer versions of Windows 10 might have Python pre-installed. You can check by typing `python` in the Command Prompt.
-   **macOS**: macOS may have an older version of Python installed by default. Use `python3` to use the newly installed version.
-   **PATH**: Adding Python to PATH makes it possible to run Python from any location in the Command Prompt or Terminal without specifying the full path to Python's executable.

