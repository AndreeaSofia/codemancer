from installer_utils import check_tool, prompt_open_url

def check_vscode_cli():
    if check_tool("code", "VS Code CLI"):
        print("✅ Found")
    else:
        print("❌ Not Found")
        prompt_open_url("VS Code CLI", "https://code.visualstudio.com/docs/editor/command-line")