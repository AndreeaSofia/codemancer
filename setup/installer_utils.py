import shutil
import webbrowser

def check_tool(command, name):
    print(f"🔍 Checking {name}...", end=" ")
    return shutil.which(command) is not None

def prompt_open_url(tool_name, url):
    choice = input(f"🛠️  {tool_name} not found. Do you want to install it now? (y/n): ").strip().lower()
    if choice == "y":
        print(f"🌐 Opening {tool_name} install page...")
        webbrowser.open(url)
        return True
    else:
        print(f"❌ Skipping {tool_name} install.")
        return False
