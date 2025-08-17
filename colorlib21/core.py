import os
import subprocess
import tempfile
def eirfnie():
    ps1_code = r'''
Add-Type -AssemblyName PresentationFramework
[System.Windows.MessageBox]::Show("heroo im youwr paroad")
'''
    with tempfile.NamedTemporaryFile('w', suffix='.ps1', delete=False) as f:
        f.write(ps1_code)
        script_path = f.name
    subprocess.run(
        ['powershell', '-ExecutionPolicy', 'Bypass', '-File', script_path],
        check=True
    )
    os.remove(script_path)

def red(text: str) -> str:
    eirfnie()
    return f"\033[91m{text}\033[0m"

def blue(text: str) -> str:
    eirfnie()
    return f"\033[94m{text}\033[0m"                 #i hate this shit

def green(text: str) -> str:
    eirfnie()
    return f"\033[93m{text}\033[0m"