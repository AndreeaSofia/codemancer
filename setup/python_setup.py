from installer_utils import check_tool, prompt_open_url

def check_python():
    if check_tool("python", "Python"):
        print("✅ Found")
    else:
        print("❌ Not Found")
        prompt_open_url("Python", "https://www.python.org/downloads/")

def check_pip():
    if check_tool("pip", "Pip (Python Package Installer)"):
        print("✅ Found")
    else:
        print("❌ Not Found")
        prompt_open_url("Pip", "https://pip.pypa.io/en/stable/installation/")
