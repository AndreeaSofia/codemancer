import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "setup")))

from setup.python_setup import check_python, check_pip
from setup.git_setup import check_git
from setup.vscode_setup import check_vscode_cli
from setup.installer_utils import check_tool, prompt_open_url

def main():
    print("\n🧙 Welcome to the Codemancer Wizard!")
    print("Let's check your magical tools...\n")

    check_python()
    check_pip()
    check_git()
    check_vscode_cli()

    print("\n✨ Setup complete! If something is missing, your spellbook will help you install it.")

if __name__ == "__main__":
    main()
