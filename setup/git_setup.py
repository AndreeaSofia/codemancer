from installer_utils import check_tool, prompt_open_url

def check_git():
    if check_tool("git", "Git"):
        print("✅ Found")
    else:
        print("❌ Not Found")
        prompt_open_url("Git", "https://git-scm.com/downloads")