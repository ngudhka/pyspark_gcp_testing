## Installation/requirements 
To get this project up and running, you'll need to follow these steps. Please ensure you have the
necessary access and permissions internally at Ford before proceeding with data-related steps.

### 1. Prerequisites
Make sure you have the following software and access permissions:

*   **Python:** Version 3.11.8 or lower is recommended. You can download it from [python.org](https://www.python.org/downloads/).
*   **Git:** For cloning the repository. Download from [git-scm.com](https://git-scm.com/downloads).
*   **Java:** Download and install Java version 18. Download from corporate repository.

### 2. Get the Code

First, clone the project repository from GitHub:

```bash/powershell
git clone https://github.com/UoN-CS/zdat3002-coursework-1-2025-ngudhka
```

Navigate into the project directory:

```bash/powershell
cd [zdat3002-coursework-1-2025-ngudhka]
```

### 3. Set up the Python Environment

*   **Create a virtual environment:**

    Using a virtual environment is best practice to keep the libraries needed for this project separate from other Python projects you might have. This prevents version conflicts and keeps your global Python environment clean.

    First, create the virtual environment. Run this command from the project's root directory (where `README.md` is located):
    
    *   Using `venv` (standard for Python 3):
        ```bash/Powershell
        python -m venv .venv
        ```

*   **Activate the virtual environment:**
    
    The command to activate depends on your operating system and the shell you are using:
    
    *   **Git Bash / macOS / Linux:**
        ```bash
        source .venv/bin/activate
        ```

    *   **Windows PowerShell:**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```

    Your command prompt should now show `(.venv)` at the beginning, indicating the environment is
    active.
    
    **Update Pip:**

    It's a good idea to ensure your `pip` installer is up to date within the new virtual environment. **Ensure your `.venv` is activated** before running this command.

        ```bash/Powershell
        python -m pip install --upgrade pip
        ```

*   **Install project packages:**
    With the virtual environment activated, install the required Python libraries listed in the `requirements.txt` file.

    ```bash/Powershell
    pip install -r requirements.txt
    ```

### 4. Verify Setup

At this point, you should have:
*   All necessary software and drivers installed.
*   The project code cloned.
*   A virtual environment created and activated with all Python packages installed.

You are now ready to use the project.



