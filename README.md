# Simple remote executable python keylogger with pynput

## FOR EDUCATIONAL PURPOSES ONLY - USE ONLY ON SYSTEMS YOU OWN

This is a Python-based remote keylogger that captures keystrokes and sends them to a [web server](https://github.com/AntonMartic/flask-server).

### Installation & Setup
1. Clone the repository
   ```bash
    git clone https://github.com/AntonMartic/python-keylogger.git
    cd python-keylogger
    ```
2. Create and activate virtual environment
   ```bash
    # macOS/Linux
    python -m venv keylogger_env
    source keylogger_env/bin/activate
    
    # Windows
    python -m venv keylogger_env
    keylogger_env\Scripts\activate
    ```
3. Install dependencies
   ```bash
    pip install -r requirements.txt
    ```
4. Setup your server
5. Run the keylogger
   ```bash
    python keylogger_exe.py
    ```
   
### Building Executable (EXE)
Create standalone executable:
```bash
# Build EXE with console (recommended for testing)
pyinstaller --onefile --console keylogger_exe.py

# Build EXE without console (runs in background)
pyinstaller --onefile --windowed keylogger_exe.py
```


